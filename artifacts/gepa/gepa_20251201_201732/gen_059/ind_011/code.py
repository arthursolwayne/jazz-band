
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum notes
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=90, pitch=snare, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=hihat, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (38), Bb (43), C (37), F (38)
    (38, 1.5), (43, 1.875), (37, 2.25), (38, 2.625),
    # Bar 3: Bb (43), F (38), Bb (43), F (38)
    (43, 3.0), (38, 3.375), (43, 3.75), (38, 4.125),
    # Bar 4: C (37), G (42), C (37), G (42)
    (37, 4.5), (42, 4.875), (37, 5.25), (42, 5.625)
]
for pitch, time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    # Bar 2
    (65, 1.5), (68, 1.5), (69, 1.5), (72, 1.5),  # Fmaj7
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (62, 3.0), (65, 3.0), (67, 3.0), (69, 3.0),  # Bb7
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (60, 4.5), (64, 4.5), (67, 4.5), (69, 4.5)   # Cm7
]
for pitch, time in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (69) - Bb (62) - E (67) - F (69)
sax_notes = [
    (69, 1.5), (62, 1.5), (67, 1.5), (69, 1.5),
    (69, 2.625), (62, 2.625), (67, 2.625), (69, 2.625)
]
for pitch, time in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums: Bars 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=90, pitch=snare, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=hihat, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
