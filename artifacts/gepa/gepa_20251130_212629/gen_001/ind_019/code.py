
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (0.0, 36, 100),  # Kick on beat 1
    (0.75, 42, 100), # Hihat on &1
    (1.0, 38, 100),  # Snare on beat 2
    (1.5, 36, 100),  # Kick on beat 3
    (2.25, 42, 100), # Hihat on &3
    (2.5, 38, 100),  # Snare on beat 4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2: Everyone enters

# Marcus: Walking line in Fm
bass_notes = [
    (1.5, 44, 100),  # F
    (1.75, 43, 100), # Eb
    (2.0, 45, 100),  # Gb
    (2.25, 44, 100), # F
    (2.5, 41, 100),  # D
    (2.75, 43, 100), # Eb
    (3.0, 45, 100),  # Gb
    (3.25, 44, 100), # F
    (3.5, 41, 100),  # D
    (3.75, 43, 100), # Eb
    (4.0, 45, 100),  # Gb
    (4.25, 44, 100), # F
    (4.5, 41, 100),  # D
    (4.75, 43, 100), # Eb
    (5.0, 45, 100),  # Gb
    (5.25, 44, 100), # F
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (1.75, 45, 100),  # Gb7 (Fm7)
    (2.25, 50, 100),  # C7
    (3.25, 45, 100),  # Gb7
    (3.75, 50, 100),  # C7
    (4.75, 45, 100),  # Gb7
    (5.25, 50, 100),  # C7
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36, 100),  # Kick on beat 1
    (1.75, 42, 100), # Hihat on &1
    (2.0, 38, 100),  # Snare on beat 2
    (2.25, 42, 100), # Hihat on &2
    (2.5, 36, 100),  # Kick on beat 3
    (2.75, 42, 100), # Hihat on &3
    (3.0, 38, 100),  # Snare on beat 4
    (3.25, 42, 100), # Hihat on &4
    (3.5, 36, 100),  # Kick on beat 1
    (3.75, 42, 100), # Hihat on &1
    (4.0, 38, 100),  # Snare on beat 2
    (4.25, 42, 100), # Hihat on &2
    (4.5, 36, 100),  # Kick on beat 3
    (4.75, 42, 100), # Hihat on &3
    (5.0, 38, 100),  # Snare on beat 4
    (5.25, 42, 100), # Hihat on &4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Dante: Tenor sax - one short motif, make it sing
sax_notes = [
    (1.5, 62, 100),  # D
    (1.75, 66, 100), # G
    (2.0, 62, 100),  # D
    (2.5, 66, 100),  # G
    (2.75, 64, 100), # F
    (3.0, 62, 100),  # D
    (3.5, 66, 100),  # G
    (3.75, 64, 100), # F
    (4.0, 62, 100),  # D
    (4.25, 66, 100), # G
    (4.5, 64, 100),  # F
    (5.0, 62, 100),  # D
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
