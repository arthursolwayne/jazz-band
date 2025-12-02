
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

# Bass line: Marcus, walking line in F, chromatic approaches
bass_notes = [
    (45, 1.5), (46, 1.875), (44, 2.25), (43, 2.625),
    (45, 3.0), (46, 3.375), (44, 3.75), (43, 4.125),
    (45, 4.5), (46, 4.875), (44, 5.25), (43, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: Diane, 7th chords on 2 and 4, comp on 2 and 4
# F7 on 2, Bb7 on 4
piano_notes = [
    # Bar 2: F7 on beat 2
    (64, 2.625), (67, 2.625), (69, 2.625), (71, 2.625),
    # Bar 3: Bb7 on beat 4
    (62, 4.125), (65, 4.125), (67, 4.125), (69, 4.125),
    # Bar 4: F7 on beat 2
    (64, 5.625), (67, 5.625), (69, 5.625), (71, 5.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: Dante, motif - start on F (65), play F, Ab, Bb, rest on 1
sax_notes = [
    (65, 1.5), (67, 1.875), (69, 2.25), (65, 2.625),
    (65, 3.0), (67, 3.375), (69, 3.75), (65, 4.125),
    (65, 4.5), (67, 4.875), (69, 5.25), (65, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    kick_time = start
    snare_time = start + 0.375
    hihat_time = start + 0.375
    kick_time2 = start + 0.75
    snare_time2 = start + 1.125
    hihat_time2 = start + 1.125
    kick_time3 = start + 1.5
    snare_time3 = start + 1.875
    hihat_time3 = start + 1.875
    kick_time4 = start + 2.25
    snare_time4 = start + 2.625
    hihat_time4 = start + 2.625

    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_time2, end=kick_time2 + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_time2, end=snare_time2 + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_time2, end=hihat_time2 + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_time3, end=kick_time3 + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_time3, end=snare_time3 + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_time3, end=hihat_time3 + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_time4, end=kick_time4 + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_time4, end=snare_time4 + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_time4, end=hihat_time4 + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
