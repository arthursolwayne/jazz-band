
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

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (62, 1.5), (64, 1.875), (63, 2.25), (60, 2.625), # Bar 2
    (62, 3.0), (64, 3.375), (63, 3.75), (60, 4.125), # Bar 3
    (62, 4.5), (64, 4.875), (63, 5.25), (60, 5.625)  # Bar 4
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 2.25), (67, 2.25), (69, 2.25), (71, 2.25), # D7 on beat 2 of bar 2
    (64, 3.75), (67, 3.75), (69, 3.75), (71, 3.75), # D7 on beat 2 of bar 3
    (64, 5.25), (67, 5.25), (69, 5.25), (71, 5.25)  # D7 on beat 2 of bar 4
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Drums: Bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    drum_notes = [
        (36, start), (38, start + 0.375), (42, start), (42, start + 0.125), (42, start + 0.25), (42, start + 0.375),
        (36, start + 0.75), (38, start + 1.125), (42, start + 0.75), (42, start + 0.875), (42, start + 1.0), (42, start + 1.125)
    ]
    for note, time in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62), F# (66), G (67), D (62)
sax_notes = [
    (62, 1.5), (66, 1.5), (67, 1.5), (62, 1.5), # Start motif
    (62, 2.625), (66, 2.625), (67, 2.625), (62, 2.625), # Repeat motif
    (62, 3.75), (66, 3.75), (67, 3.75), (62, 3.75), # Repeat motif
    (64, 4.875), (67, 4.875), (69, 4.875), (71, 4.875)  # End with a D7 chord
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
