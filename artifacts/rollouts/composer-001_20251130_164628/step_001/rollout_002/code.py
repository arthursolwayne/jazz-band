
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

# Bass line: walking line with chromatic approaches
bass_notes = [
    (62, 1.5, 0.375), (63, 1.875, 0.375), (60, 2.25, 0.375), (61, 2.625, 0.375),
    (62, 3.0, 0.375), (63, 3.375, 0.375), (60, 3.75, 0.375), (61, 4.125, 0.375),
    (62, 4.5, 0.375), (63, 4.875, 0.375), (60, 5.25, 0.375), (61, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (64, 1.875, 0.375), (67, 1.875, 0.375), (69, 1.875, 0.375), (71, 1.875, 0.375),
    (64, 2.625, 0.375), (67, 2.625, 0.375), (69, 2.625, 0.375), (71, 2.625, 0.375),
    # Bar 3
    (64, 3.375, 0.375), (67, 3.375, 0.375), (71, 3.375, 0.375), (72, 3.375, 0.375),
    (64, 4.125, 0.375), (67, 4.125, 0.375), (71, 4.125, 0.375), (72, 4.125, 0.375),
    # Bar 4
    (64, 4.875, 0.375), (67, 4.875, 0.375), (69, 4.875, 0.375), (71, 4.875, 0.375),
    (64, 5.625, 0.375), (67, 5.625, 0.375), (69, 5.625, 0.375), (71, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(2, 5):
    bar_start = bar * 1.5
    kick1 = (36, bar_start, 0.375)
    snare1 = (38, bar_start + 0.375, 0.375)
    hihat1 = (42, bar_start, 0.1875)
    hihat2 = (42, bar_start + 0.1875, 0.1875)
    hihat3 = (42, bar_start + 0.375, 0.1875)
    hihat4 = (42, bar_start + 0.5625, 0.1875)
    kick2 = (36, bar_start + 0.75, 0.375)
    snare2 = (38, bar_start + 1.125, 0.375)
    hihat5 = (42, bar_start + 0.75, 0.1875)
    hihat6 = (42, bar_start + 0.9375, 0.1875)
    hihat7 = (42, bar_start + 1.125, 0.1875)
    hihat8 = (42, bar_start + 1.3125, 0.1875)
    drum_notes.extend([kick1, snare1, hihat1, hihat2, hihat3, hihat4, kick2, snare2, hihat5, hihat6, hihat7, hihat8])
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Melody - short motif, make it sing
sax_notes = [
    (62, 1.5, 0.5),  # Start the motif
    (64, 2.0, 0.5),  # One note up
    (62, 2.5, 0.5),  # Back down
    (60, 3.0, 0.5),  # Half step down
    (62, 3.5, 0.5),  # Back up
    (64, 4.0, 0.5),  # One more step up
    (62, 4.5, 0.5),  # Back down to the root
    (60, 5.0, 0.5)   # End on the 7th
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
