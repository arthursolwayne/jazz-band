
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
    (36, 0.75), (38, 0.875), (42, 0.75), (42, 0.875), (42, 1.0), (42, 1.125),
    (42, 1.25), (42, 1.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line with chromatic approaches
bass_notes = [
    (19, 1.5), (21, 1.875), (20, 2.25), (22, 2.625),
    (22, 3.0), (24, 3.375), (23, 3.75), (25, 4.125),
    (25, 4.5), (27, 4.875), (26, 5.25), (28, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    (53, 1.5), (50, 1.5), (57, 1.5), (55, 1.5),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (58, 2.625), (62, 2.625), (53, 2.625), (50, 2.625),
    # Bar 4: E7 (E, G#, B, D)
    (60, 3.75), (64, 3.75), (67, 3.75), (62, 3.75)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax (Dante): One short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    (53, 1.5), (55, 1.875), (53, 2.25), (55, 2.625),  # Ab, Bb, Ab, Bb
    (57, 3.75), (55, 4.125), (53, 4.5), (55, 4.875)   # C, Bb, Ab, Bb
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    drum_notes = [
        (36, start), (38, start + 0.375), (42, start), (42, start + 0.125),
        (42, start + 0.25), (42, start + 0.375),
        (36, start + 0.75), (38, start + 0.875), (42, start + 0.75), (42, start + 0.875),
        (42, start + 1.0), (42, start + 1.125), (42, start + 1.25), (42, start + 1.375)
    ]
    for note, time in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
