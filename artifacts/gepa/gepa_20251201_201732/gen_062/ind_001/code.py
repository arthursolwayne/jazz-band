
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
            note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.125)
            drums.notes.append(note)
        for subbeat in range(2):
            note = pretty_midi.Note(velocity=80, pitch=hihat, start=time + subbeat * 0.1875, end=time + subbeat * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2, measure 1
    (38, 0.0), (40, 0.375), (38, 0.75), (41, 1.125),
    # Bar 3, measure 2
    (43, 1.5), (41, 1.875), (43, 2.25), (40, 2.625),
    # Bar 4, measure 3
    (38, 3.0), (40, 3.375), (38, 3.75), (41, 4.125),
    # Bar 5, measure 4
    (43, 4.5), (41, 4.875), (43, 5.25), (40, 5.625)
]
for pitch, time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time + 1.5, end=time + 1.5 + 0.125)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (53, 1.5), (56, 1.5), (58, 1.5), (60, 1.5), # F, Ab, C, D
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (57, 1.5 + 1.5), (60, 1.5 + 1.5), (53, 1.5 + 1.5), (56, 1.5 + 1.5),
    # Bar 4: Eb7 (Eb, G, Bb, D)
    (55, 1.5 + 3.0), (58, 1.5 + 3.0), (57, 1.5 + 3.0), (60, 1.5 + 3.0),
    # Bar 5: Gm7 (G, Bb, D, F)
    (60, 1.5 + 4.5), (62, 1.5 + 4.5), (65, 1.5 + 4.5), (67, 1.5 + 4.5)
]
for pitch, time in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.5)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm motif: F, Ab, G, F (MIDI 53, 56, 60, 53)
sax_notes = [
    # Bar 2: F, Ab, G, F
    (53, 1.5), (56, 1.5 + 0.375), (60, 1.5 + 0.75), (53, 1.5 + 1.125),
    # Bar 3: leave it hanging (no notes)
    # Bar 4: repeat motif
    (53, 1.5 + 3.0), (56, 1.5 + 3.375), (60, 1.5 + 3.75), (53, 1.5 + 4.125)
]
for pitch, time in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums: Bars 2-4
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.125)
            drums.notes.append(note)
        for subbeat in range(2):
            note = pretty_midi.Note(velocity=80, pitch=hihat, start=time + subbeat * 0.1875, end=time + subbeat * 0.1875 + 0.0625)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
