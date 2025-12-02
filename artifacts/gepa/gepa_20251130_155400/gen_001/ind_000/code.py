
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
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5, 1.625), (64, 1.625, 1.75), (63, 1.75, 1.875), (60, 1.875, 2.0),
    (62, 2.0, 2.125), (64, 2.125, 2.25), (63, 2.25, 2.375), (60, 2.375, 2.5),
    (62, 2.5, 2.625), (64, 2.625, 2.75), (63, 2.75, 2.875), (60, 2.875, 3.0),
    (62, 3.0, 3.125), (64, 3.125, 3.25), (63, 3.25, 3.375), (60, 3.375, 3.5),
    (62, 3.5, 3.625), (64, 3.625, 3.75), (63, 3.75, 3.875), (60, 3.875, 4.0),
    (62, 4.0, 4.125), (64, 4.125, 4.25), (63, 4.25, 4.375), (60, 4.375, 4.5),
    (62, 4.5, 4.625), (64, 4.625, 4.75), (63, 4.75, 4.875), (60, 4.875, 5.0)
]
for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Piano (Diane): 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (64, 1.5, 1.625), (67, 1.5, 1.625), (69, 1.5, 1.625), (72, 1.5, 1.625),  # Dm7
    (67, 1.75, 1.875), (70, 1.75, 1.875), (72, 1.75, 1.875), (74, 1.75, 1.875),  # G7
    # Bar 3
    (64, 2.25, 2.375), (67, 2.25, 2.375), (69, 2.25, 2.375), (72, 2.25, 2.375),  # Dm7
    (67, 2.5, 2.625), (70, 2.5, 2.625), (72, 2.5, 2.625), (74, 2.5, 2.625),  # G7
    # Bar 4
    (64, 3.0, 3.125), (67, 3.0, 3.125), (69, 3.0, 3.125), (72, 3.0, 3.125),  # Dm7
    (67, 3.25, 3.375), (70, 3.25, 3.375), (72, 3.25, 3.375), (74, 3.25, 3.375),  # G7
    (64, 3.75, 3.875), (67, 3.75, 3.875), (69, 3.75, 3.875), (72, 3.75, 3.875),  # Dm7
    (67, 4.0, 4.125), (70, 4.0, 4.125), (72, 4.0, 4.125), (74, 4.0, 4.125)  # G7
]
for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Drums: continue the pattern (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
for bar in range(2, 5):
    bar_start = bar * 1.5
    drum_notes = [
        (36, bar_start + 0.0), (38, bar_start + 0.375), (42, bar_start + 0.375),
        (36, bar_start + 0.75), (38, bar_start + 1.125), (42, bar_start + 1.125),
        (36, bar_start + 1.5), (38, bar_start + 1.875), (42, bar_start + 1.875)
    ]
    for note, time in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax (Dante): Motif in Dm, short, singable, leaves it hanging
# Motif: D - F - G - Bb (Dm triad with extension), played as 8th notes
sax_notes = [
    (62, 1.5, 1.625), (64, 1.625, 1.75), (65, 1.75, 1.875), (67, 1.875, 2.0),
    (62, 2.0, 2.125), (64, 2.125, 2.25), (65, 2.25, 2.375), (67, 2.375, 2.5),
    (62, 2.5, 2.625), (64, 2.625, 2.75), (65, 2.75, 2.875), (67, 2.875, 3.0),
    (62, 3.0, 3.125), (64, 3.125, 3.25), (65, 3.25, 3.375), (67, 3.375, 3.5)
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
