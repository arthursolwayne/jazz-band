
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875), (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875),
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: D (D4), F#, A, B, D
sax_notes = [
    (62, 1.5, 0.375),  # D4
    (66, 1.875, 0.375),  # F#
    (69, 2.25, 0.375),   # A
    (71, 2.625, 0.375),  # B
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line starting on D (D3), chromatic approach
bass_notes = [
    (50, 1.5, 0.375),   # D3
    (51, 1.875, 0.375),  # Eb3
    (49, 2.25, 0.375),   # C3
    (50, 2.625, 0.375),  # D3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 (Bm7, G7)
piano_notes = [
    # Bm7: B, D, F#, A (bar 2, beat 2)
    (71, 1.875, 0.375), (66, 1.875, 0.375), (62, 1.875, 0.375), (69, 1.875, 0.375),
    # G7: G, B, D, F (bar 2, beat 4)
    (67, 2.625, 0.375), (71, 2.625, 0.375), (62, 2.625, 0.375), (65, 2.625, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody: E (E4), G#, B, D, F#
sax_notes = [
    (64, 3.0, 0.375),  # E4
    (69, 3.375, 0.375),  # G#
    (71, 3.75, 0.375),   # B
    (66, 4.125, 0.375),  # F#
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line starting on D (D3), chromatic approach
bass_notes = [
    (50, 3.0, 0.375),   # D3
    (51, 3.375, 0.375),  # Eb3
    (49, 3.75, 0.375),   # C3
    (50, 4.125, 0.375),  # D3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 (Em7, C7)
piano_notes = [
    # Em7: E, G, B, D (bar 3, beat 2)
    (64, 3.375, 0.375), (67, 3.375, 0.375), (71, 3.375, 0.375), (62, 3.375, 0.375),
    # C7: C, E, G, Bb (bar 3, beat 4)
    (60, 4.125, 0.375), (64, 4.125, 0.375), (67, 4.125, 0.375), (62, 4.125, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody: D (D4), F#, A, B, D (restatement with a twist)
sax_notes = [
    (62, 4.5, 0.375),  # D4
    (66, 4.875, 0.375),  # F#
    (69, 5.25, 0.375),   # A
    (71, 5.625, 0.375),  # B
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line starting on D (D3), chromatic approach
bass_notes = [
    (50, 4.5, 0.375),   # D3
    (51, 4.875, 0.375),  # Eb3
    (49, 5.25, 0.375),   # C3
    (50, 5.625, 0.375),  # D3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 (Gm7, D7)
piano_notes = [
    # Gm7: G, Bb, D, F (bar 4, beat 2)
    (67, 4.875, 0.375), (62, 4.875, 0.375), (62, 4.875, 0.375), (65, 4.875, 0.375),
    # D7: D, F#, A, C (bar 4, beat 4)
    (62, 5.625, 0.375), (66, 5.625, 0.375), (69, 5.625, 0.375), (60, 5.625, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: bar 3 and 4 (3.0 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [3.0, 4.5]:
    for i in range(4):
        start = bar + i * 0.375
        if i % 2 == 0:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
        else:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.375))
    for i in range(8):
        start = bar + i * 0.1875
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.1875))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
