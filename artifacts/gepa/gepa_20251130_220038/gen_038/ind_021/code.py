
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (0.0, 36, 100),   # Kick on beat 1
    (0.75, 42, 100),  # Hihat on &1
    (1.125, 42, 100), # Hihat on &2
    (1.5, 38, 100),   # Snare on beat 2
    (2.25, 42, 100),  # Hihat on &3
    (2.625, 42, 100), # Hihat on &4
    (3.0, 36, 100),   # Kick on beat 3
    (3.75, 42, 100),  # Hihat on &1
    (4.125, 42, 100), # Hihat on &2
    (4.5, 38, 100),   # Snare on beat 4
]
for start, pitch, velocity in drum_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, no repetition
bass_notes = [
    (1.5, 48, 100),   # F (root)
    (1.875, 50, 100),  # Gb (chromatic approach)
    (2.25, 51, 100),   # G (3rd)
    (2.625, 49, 100),  # Ab (chromatic approach)
    (3.0, 50, 100),    # Gb (chromatic approach)
    (3.375, 51, 100),  # G (3rd)
    (3.75, 53, 100),   # A (5th)
    (4.125, 52, 100),  # Ab (chromatic approach)
    (4.5, 53, 100),    # A (5th)
    (4.875, 55, 100),  # Bb (7th)
    (5.25, 53, 100),   # A (5th)
    (5.625, 52, 100),  # Ab (chromatic approach)
    (6.0, 51, 100),    # G (3rd)
]
for start, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4. Sharp and emotional
piano_notes = [
    (1.5, 53, 100),   # A (3rd)
    (1.875, 55, 100),  # Bb (7th)
    (2.25, 48, 100),   # F (root)
    (2.625, 51, 100),  # G (3rd)
    (3.0, 53, 100),    # A (3rd)
    (3.375, 55, 100),  # Bb (7th)
    (3.75, 50, 100),   # Gb (chromatic)
    (4.125, 52, 100),  # Ab (chromatic)
    (4.5, 55, 100),    # Bb (7th)
    (4.875, 53, 100),  # A (3rd)
    (5.25, 50, 100),   # Gb (chromatic)
    (5.625, 52, 100),  # Ab (chromatic)
]
for start, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 62, 100),   # E (7th)
    (1.75, 60, 100),  # D (5th)
    (2.0, 62, 100),   # E (7th)
    (2.25, 62, 100),  # E (7th)
    (2.5, 0, 0),      # Rest
    (2.75, 62, 100),  # E (7th)
    (3.0, 60, 100),   # D (5th)
    (3.25, 62, 100),  # E (7th)
    (3.5, 62, 100),   # E (7th)
    (3.75, 0, 0),     # Rest
    (4.0, 62, 100),   # E (7th)
    (4.25, 60, 100),  # D (5th)
    (4.5, 62, 100),   # E (7th)
    (4.75, 62, 100),  # E (7th)
    (5.0, 0, 0),      # Rest
    (5.25, 62, 100),  # E (7th)
    (5.5, 60, 100),   # D (5th)
    (5.75, 62, 100),  # E (7th)
]
for start, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25 if pitch != 0 else start + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
