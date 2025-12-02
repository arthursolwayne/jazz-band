
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 0.75), (42, 0.875), (42, 1.0), (42, 1.125)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (44, 1.5), (45, 1.875), (43, 2.25), (42, 2.625),
    (44, 3.0), (45, 3.375), (43, 3.75), (42, 4.125),
    (44, 4.5), (45, 4.875), (43, 5.25), (42, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - C7 (C E G B), on beat 2 and 4
    (60, 2.0), (64, 2.0), (67, 2.0), (71, 2.0),
    (60, 2.5), (64, 2.5), (67, 2.5), (71, 2.5),
    # Bar 3 - G7 (G B D F), on beat 2 and 4
    (67, 3.0), (71, 3.0), (69, 3.0), (65, 3.0),
    (67, 3.5), (71, 3.5), (69, 3.5), (65, 3.5),
    # Bar 4 - C7 again
    (60, 4.0), (64, 4.0), (67, 4.0), (71, 4.0),
    (60, 4.5), (64, 4.5), (67, 4.5), (71, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    kick_times = [bar_start, bar_start + 0.75]
    snare_times = [bar_start + 0.375, bar_start + 1.125]
    hihat_times = [bar_start + i * 0.125 for i in range(8)]
    for time in kick_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    for time in snare_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
    for time in hihat_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - A - Bb - F (bar 2), then repeat (bar 4)
sax_notes = [
    (65, 1.5), (68, 1.875), (66, 2.25), (65, 2.625),
    (65, 3.0), (68, 3.375), (66, 3.75), (65, 4.125),
    (65, 4.5), (68, 4.875), (66, 5.25), (65, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
