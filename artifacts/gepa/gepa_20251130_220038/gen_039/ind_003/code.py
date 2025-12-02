
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.75), # Snare on 2
    (42, 0.375, 0.75), # Hihat on 2
    (36, 0.75, 1.125), # Kick on 3
    (42, 0.75, 1.125), # Hihat on 3
    (38, 1.125, 1.5),  # Snare on 4
    (42, 1.125, 1.5),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: D4, F#4, A4, D5 (staccato, leave it hanging)

sax_notes = [
    (62, 1.5, 0.1875), # D4
    (66, 1.6875, 0.1875), # F#4
    (69, 1.875, 0.1875), # A4
    (72, 2.0625, 0.1875), # D5
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in D minor (D, C, B, A, G, F#, E, D)
bass_notes = [
    (62, 1.5, 0.375), # D4
    (60, 1.875, 0.375), # C4
    (59, 2.25, 0.375), # B3
    (67, 2.625, 0.375), # A4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (67, 1.6875, 0.375), # A4 (D7 chord)
    (70, 1.6875, 0.375), # C#5
    (62, 1.6875, 0.375), # D4
    (65, 1.6875, 0.375), # F#4
    (67, 2.25, 0.375), # A4 (D7 chord)
    (70, 2.25, 0.375), # C#5
    (62, 2.25, 0.375), # D4
    (65, 2.25, 0.375), # F#4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Answer the call with a descending line, just as loud, just as short
sax_notes = [
    (72, 3.0, 0.1875), # D5
    (69, 3.1875, 0.1875), # A4
    (66, 3.375, 0.1875), # F#4
    (62, 3.5625, 0.1875), # D4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in D minor (D, C, B, A, G, F#, E, D)
bass_notes = [
    (62, 3.0, 0.375), # D4
    (60, 3.375, 0.375), # C4
    (59, 3.75, 0.375), # B3
    (67, 4.125, 0.375), # A4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (67, 3.1875, 0.375), # A4 (D7 chord)
    (70, 3.1875, 0.375), # C#5
    (62, 3.1875, 0.375), # D4
    (65, 3.1875, 0.375), # F#4
    (67, 3.75, 0.375), # A4 (D7 chord)
    (70, 3.75, 0.375), # C#5
    (62, 3.75, 0.375), # D4
    (65, 3.75, 0.375), # F#4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.375),  # Hihat on 1
    (38, 3.375, 0.75), # Snare on 2
    (42, 3.375, 0.75), # Hihat on 2
    (36, 3.75, 1.125), # Kick on 3
    (42, 3.75, 1.125), # Hihat on 3
    (38, 4.125, 1.5),  # Snare on 4
    (42, 4.125, 1.5),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: One last phrase, same idea, one step higher
sax_notes = [
    (62, 4.5, 0.1875), # D4
    (66, 4.6875, 0.1875), # F#4
    (69, 4.875, 0.1875), # A4
    (72, 5.0625, 0.1875), # D5
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in D minor (D, C, B, A, G, F#, E, D)
bass_notes = [
    (62, 4.5, 0.375), # D4
    (60, 4.875, 0.375), # C4
    (59, 5.25, 0.375), # B3
    (67, 5.625, 0.375), # A4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (67, 4.6875, 0.375), # A4 (D7 chord)
    (70, 4.6875, 0.375), # C#5
    (62, 4.6875, 0.375), # D4
    (65, 4.6875, 0.375), # F#4
    (67, 5.25, 0.375), # A4 (D7 chord)
    (70, 5.25, 0.375), # C#5
    (62, 5.25, 0.375), # D4
    (65, 5.25, 0.375), # F#4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.375),  # Hihat on 1
    (38, 4.875, 0.75), # Snare on 2
    (42, 4.875, 0.75), # Hihat on 2
    (36, 5.25, 1.125), # Kick on 3
    (42, 5.25, 1.125), # Hihat on 3
    (38, 5.625, 1.5),  # Snare on 4
    (42, 5.625, 1.5),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
