
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

# Bass line: Marcus - walking line in F minor, chromatic approaches
bass_notes = [
    (45, 1.5), (46, 1.875), (44, 2.25), (43, 2.625),
    (45, 3.0), (46, 3.375), (44, 3.75), (43, 4.125),
    (45, 4.5), (46, 4.875), (47, 5.25), (48, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: Diane - 7th chords on 2 and 4, F7 on 2, B7 on 4, etc.
piano_notes = [
    # Bar 2
    (64, 1.875), (67, 1.875), (69, 1.875), (71, 1.875),
    (66, 2.625), (69, 2.625), (71, 2.625), (73, 2.625),
    # Bar 3
    (64, 3.875), (67, 3.875), (69, 3.875), (71, 3.875),
    (66, 4.625), (69, 4.625), (71, 4.625), (73, 4.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Drums: Bars 2-4
for bar in [2, 3, 4]:
    bar_start = (bar - 1) * 1.5
    # Kick on 1 and 3
    kick_times = [bar_start + 0.0, bar_start + 0.75]
    for time in kick_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    # Snare on 2 and 4
    snare_times = [bar_start + 0.375, bar_start + 1.125]
    for time in snare_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
    # Hihat on every eighth
    for i in range(8):
        hihat_time = bar_start + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.125))

# Sax: Dante - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, G
sax_notes = [
    (64, 1.5), (62, 1.875), (61, 2.25), (65, 2.625),
    (64, 3.0), (62, 3.375), (61, 3.75), (65, 4.125),
    (64, 4.5), (62, 4.875), (61, 5.25), (65, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
