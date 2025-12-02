
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (0.0, 36, 100),  # Kick on beat 1
    (0.75, 42, 100), # Hihat on beat 2
    (1.5, 38, 100),  # Snare on beat 3
    (2.25, 42, 100), # Hihat on beat 4
    (3.0, 36, 100),  # Kick on beat 1
    (3.75, 42, 100), # Hihat on beat 2
    (4.5, 38, 100),  # Snare on beat 3
    (5.25, 42, 100), # Hihat on beat 4
    (6.0, 36, 100),  # Kick on beat 1
    (6.75, 42, 100), # Hihat on beat 2
    (7.5, 38, 100),  # Snare on beat 3
    (8.25, 42, 100), # Hihat on beat 4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line: walking line, chromatic approaches, never the same note twice
bass_notes = [
    (1.5, 60, 100),  # C
    (2.0, 61, 100),  # C#
    (2.5, 62, 100),  # D
    (3.0, 64, 100),  # D#
    (3.5, 65, 100),  # E
    (4.0, 67, 100),  # F#
    (4.5, 69, 100),  # G#
    (5.0, 71, 100),  # A#
    (5.5, 72, 100),  # B
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 60, 100),  # C
    (1.5, 64, 100),  # E
    (1.5, 67, 100),  # G
    (1.5, 71, 100),  # Bb
    (2.0, 64, 100),  # E
    (2.0, 67, 100),  # G
    (2.0, 71, 100),  # Bb
    (2.0, 74, 100),  # D
    (2.5, 60, 100),  # C
    (2.5, 64, 100),  # E
    (2.5, 67, 100),  # G
    (2.5, 71, 100),  # Bb
    (3.0, 64, 100),  # E
    (3.0, 67, 100),  # G
    (3.0, 71, 100),  # Bb
    (3.0, 74, 100),  # D
    (3.5, 60, 100),  # C
    (3.5, 64, 100),  # E
    (3.5, 67, 100),  # G
    (3.5, 71, 100),  # Bb
    (4.0, 64, 100),  # E
    (4.0, 67, 100),  # G
    (4.0, 71, 100),  # Bb
    (4.0, 74, 100),  # D
    (4.5, 60, 100),  # C
    (4.5, 64, 100),  # E
    (4.5, 67, 100),  # G
    (4.5, 71, 100),  # Bb
    (5.0, 64, 100),  # E
    (5.0, 67, 100),  # G
    (5.0, 71, 100),  # Bb
    (5.0, 74, 100),  # D
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 66, 100),  # D
    (1.75, 69, 100), # F
    (2.0, 71, 100),  # G
    (2.25, 69, 100), # F
    (2.5, 66, 100),  # D
    (2.75, 64, 100), # E
    (3.0, 62, 100),  # D
    (3.25, 64, 100), # E
    (3.5, 66, 100),  # D
    (3.75, 69, 100), # F
    (4.0, 71, 100),  # G
    (4.25, 69, 100), # F
    (4.5, 66, 100),  # D
    (4.75, 64, 100), # E
    (5.0, 62, 100),  # D
    (5.25, 64, 100), # E
    (5.5, 66, 100),  # D
    (5.75, 69, 100), # F
    (6.0, 71, 100),  # G
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
