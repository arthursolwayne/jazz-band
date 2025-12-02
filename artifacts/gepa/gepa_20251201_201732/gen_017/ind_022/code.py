
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
    (0.0, 36, 100),  # Kick on beat 1
    (0.75, 42, 100), # Hihat on & of 1
    (1.0, 38, 100),  # Snare on beat 2
    (1.5, 36, 100),  # Kick on beat 3
    (1.75, 42, 100), # Hihat on & of 3
    (2.0, 38, 100),  # Snare on beat 4
    (2.5, 36, 100),  # Kick on beat 1
    (3.0, 38, 100),  # Snare on beat 2
    (3.25, 42, 100), # Hihat on & of 2
    (3.5, 36, 100),  # Kick on beat 3
    (3.75, 42, 100), # Hihat on & of 3
    (4.0, 38, 100),  # Snare on beat 4
    (4.25, 42, 100), # Hihat on & of 4
    (4.5, 36, 100),  # Kick on beat 1
    (4.75, 42, 100), # Hihat on & of 1
    (5.0, 38, 100),  # Snare on beat 2
    (5.25, 42, 100), # Hihat on & of 2
    (5.5, 36, 100),  # Kick on beat 3
    (5.75, 42, 100), # Hihat on & of 3
    (6.0, 38, 100)   # Snare on beat 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) walking line with chromatic approaches
# D2 -> Eb2 -> F2 -> G2 -> Ab2 -> Bb2 -> B2 -> C3
bass_notes = [
    (1.5, 38, 100), (1.75, 40, 100), (2.0, 42, 100), (2.25, 45, 100),
    (2.5, 46, 100), (2.75, 47, 100), (3.0, 49, 100)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    (1.5, 50, 100), (1.5, 52, 100), (1.5, 57, 100), (1.5, 60, 100)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Sax: First part of motif
# Dm motif: D - F - A - D (half note, quarter note, eighth note, eighth note)
sax_notes = [
    (1.5, 62, 100), (1.75, 65, 100), (2.0, 67, 100), (2.25, 62, 100)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: G2 (MIDI 43) walking line with chromatic approaches
# G2 -> Ab2 -> Bb2 -> B2 -> C3 -> Db3 -> D3 -> Eb3
bass_notes = [
    (3.0, 43, 100), (3.25, 45, 100), (3.5, 46, 100), (3.75, 47, 100),
    (4.0, 49, 100), (4.25, 50, 100), (4.5, 52, 100)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Piano: Bb7 (Bb D F Ab)
piano_notes = [
    (3.0, 53, 100), (3.0, 55, 100), (3.0, 57, 100), (3.0, 59, 100)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Sax: Second part of motif
# F - A - D (quarter note, eighth note, eighth note)
sax_notes = [
    (3.0, 65, 100), (3.25, 67, 100), (3.5, 62, 100)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: C3 (MIDI 52) walking line with chromatic approaches
# C3 -> Db3 -> D3 -> Eb3 -> E3 -> F3 -> F#3 -> G3
bass_notes = [
    (4.5, 52, 100), (4.75, 53, 100), (5.0, 55, 100), (5.25, 56, 100),
    (5.5, 57, 100), (5.75, 58, 100), (6.0, 60, 100)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Piano: Bb7 (Bb D F Ab)
piano_notes = [
    (4.5, 53, 100), (4.5, 55, 100), (4.5, 57, 100), (4.5, 59, 100)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Sax: Finish the motif
# D - F - A - D (half note)
sax_notes = [
    (4.5, 62, 100), (4.75, 65, 100), (5.0, 67, 100), (5.25, 62, 100)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Drums: Bar 3-4
drum_notes = [
    (3.0, 36, 100),  # Kick on beat 1
    (3.25, 42, 100), # Hihat on & of 1
    (3.5, 38, 100),  # Snare on beat 2
    (4.0, 36, 100),  # Kick on beat 3
    (4.25, 42, 100), # Hihat on & of 3
    (4.5, 38, 100),  # Snare on beat 4
    (4.75, 42, 100), # Hihat on & of 4
    (5.0, 36, 100),  # Kick on beat 1
    (5.25, 42, 100), # Hihat on & of 1
    (5.5, 38, 100),  # Snare on beat 2
    (5.75, 42, 100), # Hihat on & of 2
    (6.0, 36, 100)   # Kick on beat 3
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
