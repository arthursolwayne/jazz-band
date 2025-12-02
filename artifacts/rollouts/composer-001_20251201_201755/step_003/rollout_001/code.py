
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
    (0.75, 42, 100), # Hihat on &1
    (1.0, 38, 100),  # Snare on 2
    (1.25, 42, 100), # Hihat on &2
    (1.5, 36, 100),  # Kick on 3
    (1.75, 42, 100), # Hihat on &3
    (2.0, 38, 100),  # Snare on 4
    (2.25, 42, 100), # Hihat on &4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line (root, 5th, chromatic approach)
bass_notes = [
    (1.5, 50, 100), # D2 (root)
    (1.75, 53, 100), # F#2 (b3 chromatic approach)
    (2.0, 57, 100), # A2 (5th)
    (2.25, 56, 100), # G#2 (b7 chromatic approach)
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    (1.5, 67, 100), (1.5, 69, 100), (1.5, 72, 100), (1.5, 76, 100),  # Dmaj7
    (2.0, 69, 100), (2.0, 71, 100), (2.0, 75, 100), (2.0, 79, 100),  # F#7
    (2.5, 67, 100), (2.5, 70, 100), (2.5, 74, 100), (2.5, 77, 100),  # A7
    (3.0, 67, 100), (3.0, 69, 100), (3.0, 72, 100), (3.0, 76, 100),  # Dmaj7
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.5))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36, 100),  # Kick on 1
    (1.75, 42, 100), # Hihat &1
    (2.0, 38, 100),  # Snare on 2
    (2.25, 42, 100), # Hihat &2
    (2.5, 36, 100),  # Kick on 3
    (2.75, 42, 100), # Hihat &3
    (3.0, 38, 100),  # Snare on 4
    (3.25, 42, 100), # Hihat &4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62), F# (64), A (67) -> D (62)
sax_notes = [
    (1.5, 62, 100),  # D
    (1.75, 64, 100), # F#
    (2.0, 67, 100),  # A
    (3.0, 62, 100),  # D
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line (root, 5th, chromatic approach)
bass_notes = [
    (3.0, 50, 100), # D2 (root)
    (3.25, 53, 100), # F#2 (b3 chromatic approach)
    (3.5, 57, 100), # A2 (5th)
    (3.75, 56, 100), # G#2 (b7 chromatic approach)
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    (3.0, 69, 100), (3.0, 71, 100), (3.0, 75, 100), (3.0, 79, 100),  # F#7
    (3.5, 67, 100), (3.5, 70, 100), (3.5, 74, 100), (3.5, 77, 100),  # A7
    (4.0, 67, 100), (4.0, 69, 100), (4.0, 72, 100), (4.0, 76, 100),  # Dmaj7
    (4.5, 67, 100), (4.5, 69, 100), (4.5, 72, 100), (4.5, 76, 100),  # Dmaj7
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.5))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36, 100),  # Kick on 1
    (3.25, 42, 100), # Hihat &1
    (3.5, 38, 100),  # Snare on 2
    (3.75, 42, 100), # Hihat &2
    (4.0, 36, 100),  # Kick on 3
    (4.25, 42, 100), # Hihat &3
    (4.5, 38, 100),  # Snare on 4
    (4.75, 42, 100), # Hihat &4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Sax: continuation of the motif
# A (67), G# (66), A (67), D (62)
sax_notes = [
    (3.0, 67, 100),  # A
    (3.25, 66, 100), # G#
    (3.5, 67, 100),  # A
    (4.5, 62, 100),  # D
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line (root, 5th, chromatic approach)
bass_notes = [
    (4.5, 50, 100), # D2 (root)
    (4.75, 53, 100), # F#2 (b3 chromatic approach)
    (5.0, 57, 100), # A2 (5th)
    (5.25, 56, 100), # G#2 (b7 chromatic approach)
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    (4.5, 67, 100), (4.5, 69, 100), (4.5, 72, 100), (4.5, 76, 100),  # Dmaj7
    (5.0, 69, 100), (5.0, 71, 100), (5.0, 75, 100), (5.0, 79, 100),  # F#7
    (5.5, 67, 100), (5.5, 70, 100), (5.5, 74, 100), (5.5, 77, 100),  # A7
    (6.0, 67, 100), (6.0, 69, 100), (6.0, 72, 100), (6.0, 76, 100),  # Dmaj7
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.5))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36, 100),  # Kick on 1
    (4.75, 42, 100), # Hihat &1
    (5.0, 38, 100),  # Snare on 2
    (5.25, 42, 100), # Hihat &2
    (5.5, 36, 100),  # Kick on 3
    (5.75, 42, 100), # Hihat &3
    (6.0, 38, 100),  # Snare on 4
    (6.25, 42, 100), # Hihat &4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Sax: finish the motif
# D (62)
sax_notes = [
    (4.5, 62, 100),  # D
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("waynes_moment.mid")
