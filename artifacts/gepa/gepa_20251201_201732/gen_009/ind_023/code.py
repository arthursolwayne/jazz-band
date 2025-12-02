
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
    # Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.125),
    (42, 0.125, 0.125), (42, 0.25, 0.125), (42, 0.375, 0.125),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.125),
    (42, 0.875, 0.125), (42, 1.0, 0.125), (42, 1.125, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5s - 3.0s)
    (62, 1.5, 0.375), (64, 1.875, 0.375), (63, 2.25, 0.375), (60, 2.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    (62, 1.5, 0.375), (64, 1.5, 0.375), (67, 1.5, 0.375), (69, 1.5, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Melody - One short motif, make it sing
sax_notes = [
    (67, 1.5, 0.375), (69, 2.125, 0.375), (67, 2.5, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Dm7 -> Gm7
bass_notes = [
    (67, 3.0, 0.375), (69, 3.375, 0.375), (68, 3.75, 0.375), (65, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Gm7
piano_notes = [
    (65, 3.0, 0.375), (67, 3.0, 0.375), (70, 3.0, 0.375), (72, 3.0, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Continue the motif, leave it hanging
sax_notes = [
    (65, 3.0, 0.375), (67, 3.625, 0.375), (65, 4.25, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Gm7 -> C7
bass_notes = [
    (72, 4.5, 0.375), (74, 4.875, 0.375), (73, 5.25, 0.375), (70, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: C7
piano_notes = [
    (70, 4.5, 0.375), (72, 4.5, 0.375), (74, 4.5, 0.375), (77, 4.5, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Finish the motif
sax_notes = [
    (70, 4.5, 0.375), (72, 5.125, 0.375), (70, 5.75, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = []
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    drum_notes.append((36, start, 0.375))
    drum_notes.append((36, start + 0.75, 0.375))
    # Snare on 2 and 4
    drum_notes.append((38, start + 0.375, 0.375))
    drum_notes.append((38, start + 1.125, 0.375))
    # Hihat on every eighth
    for eighth in range(0, 8):
        drum_notes.append((42, start + eighth * 0.125, 0.125))

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
