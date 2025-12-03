
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
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line: F2 (D2), Bb2 (F2), C3 (Bb2), D3 (C3) with chromatic approaches
bass_notes = [
    (38, 1.5), (37, 1.6), (38, 1.7), (38, 1.875),  # F2 with F#2 approach
    (41, 2.25), (40, 2.35), (41, 2.5), (41, 2.625), # Bb2 with B approach
    (43, 3.0), (42, 3.1), (43, 3.2), (43, 3.375),  # C3 with C#3 approach
    (45, 3.75), (44, 3.85), (45, 4.0), (45, 4.125)  # D3 with D#3 approach
]
for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
    bass.notes.append(note_obj)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    (53, 1.5), (58, 1.5), (57, 1.5), (60, 1.5),  # F, A, C, E
    (53, 2.5), (58, 2.5), (57, 2.5), (60, 2.5),  # F, A, C, E
    (53, 3.5), (58, 3.5), (60, 3.5), (62, 3.5),  # F, A, E, G
    (53, 4.5), (58, 4.5), (60, 4.5), (62, 4.5)   # F, A, E, G
]
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(note_obj)

# Sax: Motif - short, singable, hanging
# F (53), Bb (58), D (62), rest
sax_notes = [
    (53, 1.5), (58, 1.75), (62, 2.0), (53, 2.5), (58, 2.75), (62, 3.0), (53, 3.5), (58, 3.75), (62, 4.0)
]
for note, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(note_obj)

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('jazz_intro.mid')
