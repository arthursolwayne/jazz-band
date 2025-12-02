
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
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hi-hat on &1
    (1.0, 38, 100),  # Snare on 2
    (1.5, 36, 100),  # Kick on 3
    (2.25, 42, 100), # Hi-hat on &3
    (2.5, 38, 100),  # Snare on 4
    (3.0, 42, 100),  # Hi-hat on 4
]

for start, pitch, velocity in drum_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 62, 100),  # F (root)
    (1.75, 63, 100),  # Gb (chromatic approach)
    (2.0, 64, 100),  # G (3rd)
    (2.25, 63, 100), # Gb (chromatic)
    (2.5, 62, 100),  # F (root)
    (2.75, 60, 100),  # Eb (7th)
    (3.0, 59, 100),  # D (flat 7)
    (3.25, 60, 100),  # Eb (7th)
    (3.5, 62, 100),  # F (root)
    (3.75, 63, 100),  # Gb (chromatic)
    (4.0, 64, 100),  # G (3rd)
    (4.25, 63, 100), # Gb (chromatic)
    (4.5, 62, 100),  # F (root)
    (4.75, 60, 100),  # Eb (7th)
    (5.0, 59, 100),  # D (flat 7)
    (5.25, 60, 100),  # Eb (7th)
]

for start, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (2.0, 62, 100),  # F7: F, A, C, Eb
    (2.0, 64, 100),
    (2.0, 60, 100),
    (2.0, 59, 100),
    # Bar 3
    (3.5, 62, 100),  # F7 again
    (3.5, 64, 100),
    (3.5, 60, 100),
    (3.5, 59, 100),
    # Bar 4
    (5.0, 62, 100),  # F7 again
    (5.0, 64, 100),
    (5.0, 60, 100),
    (5.0, 59, 100),
]

for start, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    piano.notes.append(note)

# Dante on sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 67, 100),  # Bb (Fm7)
    (1.75, 67, 100),
    (2.0, 69, 100),  # C
    (2.25, 67, 100), # Bb (leave hanging)
    (3.0, 69, 100),  # C (come back)
    (3.25, 67, 100), # Bb
    (3.5, 64, 100),  # F
    (3.75, 62, 100), # Eb
    (4.0, 64, 100),  # F
    (4.25, 69, 100), # C
    (4.5, 67, 100),  # Bb
    (4.75, 64, 100), # F
    (5.0, 62, 100),  # Eb
    (5.25, 64, 100), # F
    (5.5, 69, 100),  # C
    (5.75, 67, 100), # Bb
]

for start, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (1.5, 36, 100),  # Kick on 1
    (2.0, 38, 100),  # Snare on 2
    (2.25, 42, 100), # Hi-hat on &2
    (2.5, 36, 100),  # Kick on 3
    (3.0, 38, 100),  # Snare on 4
    (3.25, 42, 100), # Hi-hat on &4
    # Bar 3
    (3.5, 36, 100),  # Kick on 1
    (4.0, 38, 100),  # Snare on 2
    (4.25, 42, 100), # Hi-hat on &2
    (4.5, 36, 100),  # Kick on 3
    (5.0, 38, 100),  # Snare on 4
    (5.25, 42, 100), # Hi-hat on &4
    # Bar 4
    (5.5, 36, 100),  # Kick on 1
    (6.0, 38, 100),  # Snare on 2
    (6.25, 42, 100), # Hi-hat on &2
]

for start, pitch, velocity in drum_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
