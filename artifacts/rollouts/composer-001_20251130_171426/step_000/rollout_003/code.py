
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
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    (62, 1.5, 0.375), (64, 1.875, 0.375), (63, 2.25, 0.375), (60, 2.625, 0.375),
    (62, 3.0, 0.375), (64, 3.375, 0.375), (63, 3.75, 0.375), (60, 4.125, 0.375),
    (62, 4.5, 0.375), (64, 4.875, 0.375), (63, 5.25, 0.375), (60, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (61, 1.875, 0.1875), (65, 1.875, 0.1875), (67, 1.875, 0.1875), (69, 1.875, 0.1875),
    (61, 2.625, 0.1875), (65, 2.625, 0.1875), (67, 2.625, 0.1875), (69, 2.625, 0.1875),
    # Bar 3
    (61, 3.375, 0.1875), (65, 3.375, 0.1875), (67, 3.375, 0.1875), (69, 3.375, 0.1875),
    (61, 4.125, 0.1875), (65, 4.125, 0.1875), (67, 4.125, 0.1875), (69, 4.125, 0.1875),
    # Bar 4
    (61, 4.875, 0.1875), (65, 4.875, 0.1875), (67, 4.875, 0.1875), (69, 4.875, 0.1875),
    (61, 5.625, 0.1875), (65, 5.625, 0.1875), (67, 5.625, 0.1875), (69, 5.625, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    time_start = 1.5 * bar
    kick1 = (36, time_start, 0.375)
    snare2 = (38, time_start + 0.375, 0.375)
    hihat1 = (42, time_start, 0.1875)
    hihat2 = (42, time_start + 0.1875, 0.1875)
    hihat3 = (42, time_start + 0.375, 0.1875)
    hihat4 = (42, time_start + 0.5625, 0.1875)
    kick3 = (36, time_start + 0.75, 0.375)
    snare4 = (38, time_start + 1.125, 0.375)
    hihat5 = (42, time_start + 0.75, 0.1875)
    hihat6 = (42, time_start + 0.9375, 0.1875)
    hihat7 = (42, time_start + 1.125, 0.1875)
    hihat8 = (42, time_start + 1.3125, 0.1875)

    for note, start, duration in [kick1, snare2, hihat1, hihat2, hihat3, hihat4, kick3, snare4, hihat5, hihat6, hihat7, hihat8]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7: D, F, A, C
sax_notes = [
    (62, 1.5, 0.75),   # D
    (64, 2.25, 0.75),  # F
    (67, 3.0, 0.75),   # A
    (60, 3.75, 0.75),  # C
    (62, 4.5, 0.75),   # D
    (64, 5.25, 0.75)   # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
