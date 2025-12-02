
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

# Bass: Walking line in F, chromatic approaches, no repeated notes
bass_notes = [
    (45, 1.5, 0.375), (47, 1.875, 0.375), (48, 2.25, 0.375), (50, 2.625, 0.375),
    (52, 3.0, 0.375), (53, 3.375, 0.375), (55, 3.75, 0.375), (57, 4.125, 0.375),
    (59, 4.5, 0.375), (60, 4.875, 0.375), (62, 5.25, 0.375), (64, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.875, 0.1875), (67, 1.875, 0.1875), (69, 1.875, 0.1875), (71, 1.875, 0.1875),
    (62, 2.625, 0.1875), (67, 2.625, 0.1875), (69, 2.625, 0.1875), (71, 2.625, 0.1875),
    # Bar 3
    (62, 3.375, 0.1875), (67, 3.375, 0.1875), (69, 3.375, 0.1875), (71, 3.375, 0.1875),
    (62, 4.125, 0.1875), (67, 4.125, 0.1875), (69, 4.125, 0.1875), (71, 4.125, 0.1875),
    # Bar 4
    (62, 4.875, 0.1875), (67, 4.875, 0.1875), (69, 4.875, 0.1875), (71, 4.875, 0.1875),
    (62, 5.625, 0.1875), (67, 5.625, 0.1875), (69, 5.625, 0.1875), (71, 5.625, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums in bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    kick1 = (36, start, 0.375)
    snare2 = (38, start + 0.375, 0.375)
    hihat1 = (42, start, 0.1875)
    hihat2 = (42, start + 0.1875, 0.1875)
    hihat3 = (42, start + 0.375, 0.1875)
    hihat4 = (42, start + 0.5625, 0.1875)
    kick3 = (36, start + 1.125, 0.375)
    snare4 = (38, start + 1.5, 0.375)
    hihat5 = (42, start + 1.125, 0.1875)
    hihat6 = (42, start + 1.3125, 0.1875)
    hihat7 = (42, start + 1.5, 0.1875)
    hihat8 = (42, start + 1.6875, 0.1875)
    for note, s, d in [kick1, snare2, hihat1, hihat2, hihat3, hihat4, kick3, snare4, hihat5, hihat6, hihat7, hihat8]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=s, end=s + d))

# Sax: One short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    (62, 1.5, 0.375), (66, 1.875, 0.375), (67, 2.25, 0.375),
    (66, 2.625, 0.375), (62, 3.0, 0.375), (67, 3.375, 0.375),
    (69, 3.75, 0.375), (67, 4.125, 0.375), (66, 4.5, 0.375),
    (62, 4.875, 0.375), (64, 5.25, 0.375), (67, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
