
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
    (36, 0.0), (38, 0.375), (42, 0.375),  # 1
    (36, 0.75), (38, 1.125), (42, 1.125),  # 2
    (36, 1.5), (38, 1.875), (42, 1.875)    # 3
]
for note, time in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line (F2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5), (40, 1.875), (39, 2.25), (43, 2.625),  # Bar 2
    (43, 3.0), (45, 3.375), (44, 3.75), (48, 4.125),  # Bar 3
    (48, 4.5), (50, 4.875), (49, 5.25), (53, 5.625)   # Bar 4
]
for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.1)
    bass.notes.append(note_obj)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    (65, 1.5), (76, 1.5), (69, 1.5), (71, 1.5),  # Fmaj7
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (65, 3.0), (74, 3.0), (69, 3.0), (70, 3.0),  # Bb7
    # Bar 4: Dm7 (D, F, A, C)
    (67, 4.5), (76, 4.5), (71, 4.5), (69, 4.5)   # Dm7
]
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    piano.notes.append(note_obj)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F - E - D - G (motif)
sax_notes = [
    (65, 1.5), (64, 1.75), (62, 2.0), (67, 2.25),  # Start motif
    (67, 4.5), (65, 4.75), (64, 5.0), (62, 5.25)   # Return and finish
]
for note, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1)
    sax.notes.append(note_obj)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0)
for i in range(2):
    drum_notes = [
        (36, 1.5 + i * 1.5), (38, 1.5 + i * 1.5 + 0.375), (42, 1.5 + i * 1.5 + 0.375),
        (36, 1.5 + i * 1.5 + 0.75), (38, 1.5 + i * 1.5 + 1.125), (42, 1.5 + i * 1.5 + 1.125),
        (36, 1.5 + i * 1.5 + 1.5), (38, 1.5 + i * 1.5 + 1.875), (42, 1.5 + i * 1.5 + 1.875)
    ]
    for note, time in drum_notes:
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
        drums.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
