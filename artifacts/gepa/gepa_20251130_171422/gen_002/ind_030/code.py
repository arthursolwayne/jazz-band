
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
    (36, 0.0), (38, 0.375), (42, 0.0),
    (36, 1.125), (38, 1.5), (42, 1.125)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (62, 1.5, 0.25), (64, 1.75, 0.25), (63, 2.0, 0.25), (60, 2.25, 0.25),
    (62, 2.5, 0.25), (64, 2.75, 0.25), (63, 3.0, 0.25), (60, 3.25, 0.25),
    (62, 3.5, 0.25), (64, 3.75, 0.25), (63, 4.0, 0.25), (60, 4.25, 0.25),
    (62, 4.5, 0.25), (64, 4.75, 0.25), (63, 5.0, 0.25), (60, 5.25, 0.25)
]
for pitch, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (67, 2.0, 0.25), (71, 2.0, 0.25), (69, 2.0, 0.25), (72, 2.0, 0.25),
    (67, 3.0, 0.25), (71, 3.0, 0.25), (69, 3.0, 0.25), (72, 3.0, 0.25),
    (67, 4.0, 0.25), (71, 4.0, 0.25), (69, 4.0, 0.25), (72, 4.0, 0.25)
]
for pitch, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=pitch, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    drum_notes = [
        (36, bar_start, 0.125), (38, bar_start + 0.375, 0.125),
        (36, bar_start + 1.125, 0.125), (38, bar_start + 1.5, 0.125)
    ]
    for note, start, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Saxophone: short motif, make it sing
# Motif: D (62), F (65), E (64), D (62) — one measure, then hold on the last note
sax_notes = [
    (62, 1.5, 0.25), (65, 1.75, 0.25), (64, 2.0, 0.25), (62, 2.25, 0.75)
]
for pitch, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
