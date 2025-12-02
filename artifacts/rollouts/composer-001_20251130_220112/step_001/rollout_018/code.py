
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.1875), (42, 0.375), (42, 0.5625),
    (42, 0.75), (42, 0.9375), (42, 1.125), (42, 1.3125), (36, 1.5),
    (38, 1.875), (42, 1.5), (42, 1.6875), (42, 1.875), (42, 2.0625),
    (42, 2.25), (42, 2.4375), (42, 2.625), (42, 2.8125), (42, 3.0)
]

for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking with chromatic approaches
bass_notes = [
    # Bar 2
    (62, 1.5), (64, 1.875), (62, 2.25), (60, 2.625),
    # Bar 3
    (62, 3.0), (64, 3.375), (62, 3.75), (60, 4.125),
    # Bar 4
    (62, 4.5), (64, 4.875), (62, 5.25), (60, 5.625)
]

for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comping
# Bar 2: C7 on beat 2, G7 on beat 4
piano_notes = [
    # Bar 2
    (60, 1.875), (64, 1.875), (67, 1.875), (71, 1.875),  # C7
    (67, 2.625), (71, 2.625), (74, 2.625), (77, 2.625),  # G7
    # Bar 3
    (62, 3.375), (66, 3.375), (69, 3.375), (73, 3.375),  # D7
    (67, 4.125), (71, 4.125), (74, 4.125), (77, 4.125),  # G7
    # Bar 4
    (65, 4.875), (69, 4.875), (72, 4.875), (76, 4.875),  # B7
    (67, 5.625), (71, 5.625), (74, 5.625), (77, 5.625)   # G7
]

for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Sax: motif — start on D (62), move to Bb (60), then G (67), and leave it hanging
sax_notes = [
    (62, 1.5), (60, 1.75), (67, 2.0), (62, 2.25),  # Bar 2
    (67, 2.5), (64, 2.75), (62, 3.0), (60, 3.25),  # Bar 3
    (67, 3.5), (64, 3.75), (62, 4.0), (60, 4.25),  # Bar 4
    (67, 4.5), (64, 4.75), (62, 5.0), (60, 5.25)   # Bar 4
]

for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: Bar 2-4
for bar in range(2, 5):
    start_time = bar * 1.5
    # Kick on 1 and 3
    kick_times = [start_time, start_time + 0.75]
    for t in kick_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.125))
    # Snare on 2 and 4
    snare_times = [start_time + 0.375, start_time + 1.125]
    for t in snare_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.125))
    # Hi-hat on every eighth
    hihat_times = [start_time + i * 0.375 for i in range(4)]
    for t in hihat_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
