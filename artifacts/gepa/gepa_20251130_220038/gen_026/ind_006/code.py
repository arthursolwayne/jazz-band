
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.75, 0.375), # Snare on 2
    (42, 0.0, 0.1875), # Hihat on 1
    (42, 0.1875, 0.1875), # Hihat on &
    (42, 0.375, 0.1875), # Hihat on 2
    (42, 0.5625, 0.1875), # Hihat on &
    (42, 0.75, 0.1875), # Hihat on 3
    (42, 0.9375, 0.1875), # Hihat on &
    (36, 1.125, 0.375), # Kick on 3
    (42, 1.125, 0.1875), # Hihat on 3
    (42, 1.3125, 0.1875), # Hihat on &
    (38, 1.5, 0.375), # Snare on 4
    (42, 1.5, 0.1875), # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    (58, 1.5, 0.375), # D
    (59, 1.875, 0.375), # D#
    (60, 2.25, 0.375), # E
    (57, 2.625, 0.375), # C#
    # Bar 3
    (62, 3.0, 0.375), # F#
    (60, 3.375, 0.375), # E
    (59, 3.75, 0.375), # D#
    (61, 4.125, 0.375), # F
    # Bar 4
    (62, 4.5, 0.375), # F#
    (64, 4.875, 0.375), # G#
    (65, 5.25, 0.375), # A
    (63, 5.625, 0.375), # G
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (comp on 2 and 4)
    (62, 1.875, 0.1875), # F#7 (F#, A#, D#, F#)
    (67, 1.875, 0.1875),
    (64, 1.875, 0.1875),
    (62, 1.875, 0.1875),
    (62, 2.25, 0.1875), # F#7 on 4
    (67, 2.25, 0.1875),
    (64, 2.25, 0.1875),
    (62, 2.25, 0.1875),
    # Bar 3 (comp on 2 and 4)
    (62, 3.375, 0.1875), # F#7 again
    (67, 3.375, 0.1875),
    (64, 3.375, 0.1875),
    (62, 3.375, 0.1875),
    (62, 3.75, 0.1875), # F#7 on 4
    (67, 3.75, 0.1875),
    (64, 3.75, 0.1875),
    (62, 3.75, 0.1875),
    # Bar 4 (comp on 2 and 4)
    (62, 4.875, 0.1875), # F#7 again
    (67, 4.875, 0.1875),
    (64, 4.875, 0.1875),
    (62, 4.875, 0.1875),
    (62, 5.25, 0.1875), # F#7 on 4
    (67, 5.25, 0.1875),
    (64, 5.25, 0.1875),
    (62, 5.25, 0.1875),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    (62, 1.5, 0.375), # D (start of motif)
    (66, 1.875, 0.375), # F#
    (69, 2.25, 0.375), # A (end of motif)
    # Bar 3
    (62, 3.0, 0.375), # D (repeat motif)
    (66, 3.375, 0.375), # F#
    (71, 3.75, 0.375), # C (variation)
    # Bar 4
    (62, 4.5, 0.375), # D (return to motif)
    (66, 4.875, 0.375), # F#
    (69, 5.25, 0.375), # A (end with a cry)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add drum fills in bar 4
drum_notes = [
    (36, 5.625, 0.375), # Kick on 3
    (38, 6.0, 0.375), # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add hihat throughout bar 4
for i in range(4):
    hihat_start = 4.5 + i * 0.375
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_start + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
