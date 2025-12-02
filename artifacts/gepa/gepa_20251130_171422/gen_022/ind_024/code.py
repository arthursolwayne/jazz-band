
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
    (36, 0.0, 0.375), (42, 0.0, 0.125),
    (38, 0.375, 0.125), (42, 0.375, 0.125),
    (36, 0.75, 0.375), (42, 0.75, 0.125),
    (38, 1.125, 0.125), (42, 1.125, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    (40, 1.5, 0.375), (39, 1.875, 0.375), (40, 2.25, 0.375), (38, 2.625, 0.375),
    (37, 2.875, 0.375), (38, 3.25, 0.375), (39, 3.625, 0.375), (40, 4.0, 0.375),
    (41, 4.375, 0.375), (42, 4.75, 0.375), (43, 5.125, 0.375), (44, 5.5, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (42, 1.5, 0.125), (45, 1.5, 0.125), (48, 1.5, 0.125), (50, 1.5, 0.125),
    (43, 2.0, 0.125), (46, 2.0, 0.125), (49, 2.0, 0.125), (51, 2.0, 0.125),
    # Bar 3
    (42, 2.5, 0.125), (45, 2.5, 0.125), (48, 2.5, 0.125), (50, 2.5, 0.125),
    (43, 3.0, 0.125), (46, 3.0, 0.125), (49, 3.0, 0.125), (51, 3.0, 0.125),
    # Bar 4
    (42, 3.5, 0.125), (45, 3.5, 0.125), (48, 3.5, 0.125), (50, 3.5, 0.125),
    (43, 4.0, 0.125), (46, 4.0, 0.125), (49, 4.0, 0.125), (51, 4.0, 0.125)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=110, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=110, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.5)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.25)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.125)
    hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.125, end=start + 0.25)
    hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.25, end=start + 0.375)
    hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.5)
    hihat5 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.5, end=start + 0.625)
    hihat6 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.625, end=start + 0.75)
    hihat7 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 0.875)
    hihat8 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.875, end=start + 1.0)
    hihat9 = pretty_midi.Note(velocity=90, pitch=42, start=start + 1.0, end=start + 1.125)
    hihat10 = pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.25)
    hihat11 = pretty_midi.Note(velocity=90, pitch=42, start=start + 1.25, end=start + 1.375)
    hihat12 = pretty_midi.Note(velocity=90, pitch=42, start=start + 1.375, end=start + 1.5)
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
    drums.notes.append(hihat9)
    drums.notes.append(hihat10)
    drums.notes.append(hihat11)
    drums.notes.append(hihat12)

# Sax: One short motif, sparse but expressive
# Motif: Fm (F, Ab, Bb) with a slight chromatic twist
sax_notes = [
    # Bar 2
    (40, 1.5, 0.375), (42, 1.875, 0.375), (41, 2.25, 0.375),
    # Bar 3
    (40, 2.625, 0.375), (42, 2.875, 0.25), (41, 3.125, 0.25),
    # Bar 4
    (40, 3.375, 0.375), (42, 3.75, 0.375), (41, 4.125, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.dump()  # Save the MIDI file
