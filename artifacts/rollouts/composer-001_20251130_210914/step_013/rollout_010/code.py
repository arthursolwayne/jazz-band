
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.125, 0.375)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    (48, 1.5, 0.375), (50, 1.875, 0.375), (49, 2.25, 0.375), (52, 2.625, 0.375),
    (53, 2.875, 0.375), (51, 3.25, 0.375), (50, 3.625, 0.375), (48, 4.0, 0.375),
    (49, 4.375, 0.375), (51, 4.75, 0.375), (52, 5.125, 0.375), (50, 5.5, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2
    (64, 1.5, 0.1875), (67, 1.5, 0.1875), (71, 1.5, 0.1875), (72, 1.5, 0.1875),
    (68, 1.875, 0.1875), (71, 1.875, 0.1875), (74, 1.875, 0.1875), (76, 1.875, 0.1875),
    # Bar 3
    (64, 2.25, 0.1875), (67, 2.25, 0.1875), (71, 2.25, 0.1875), (72, 2.25, 0.1875),
    (68, 2.625, 0.1875), (71, 2.625, 0.1875), (74, 2.625, 0.1875), (76, 2.625, 0.1875),
    # Bar 4
    (64, 3.0, 0.1875), (67, 3.0, 0.1875), (71, 3.0, 0.1875), (72, 3.0, 0.1875),
    (68, 3.375, 0.1875), (71, 3.375, 0.1875), (74, 3.375, 0.1875), (76, 3.375, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.1875)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.1875, end=start + 0.375)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.5625)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.5625, end=start + 0.75)
    hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.9375)
    hihat6 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.9375, end=start + 1.125)
    hihat7 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.3125)
    hihat8 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.3125, end=start + 1.5)
    # Append all
    drums.notes.append(kick1)
    drums.notes.append(kick2)
    drums.notes.append(snare1)
    drums.notes.append(snare2)
    drums.notes.append(hihat1)
    drums.notes.append(hihat2)
    drums.notes.append(hihat3)
    drums.notes.append(hihat4)
    drums.notes.append(hihat5)
    drums.notes.append(hihat6)
    drums.notes.append(hihat7)
    drums.notes.append(hihat8)

# Sax: Motif in F, one short phrase with a twist
# F, Bb, G, Ab, F
sax_notes = [
    (87, 1.5, 0.375), (82, 1.875, 0.375), (84, 2.25, 0.375), (85, 2.625, 0.375),
    (87, 2.875, 0.375), (82, 3.25, 0.375), (84, 3.625, 0.375), (85, 4.0, 0.375),
    (87, 4.375, 0.375), (82, 4.75, 0.375), (84, 5.125, 0.375), (85, 5.5, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
