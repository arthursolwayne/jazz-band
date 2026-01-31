
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
for beat in range(4):
    time = beat * 0.375
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5), (40, 1.75), (39, 2.0), (43, 2.25),  # Bar 2
    (41, 2.5), (43, 2.75), (42, 3.0), (46, 3.25),  # Bar 3
    (44, 3.5), (46, 3.75), (45, 4.0), (49, 4.25)   # Bar 4
]
for pitch, time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: open voicings, different chord each bar, resolve on the last
# Chords: Fm7, Bbm7, Eb7, Am7
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (53, 1.5), (55, 1.5), (57, 1.5), (58, 1.5),
    # Bar 3: Bbm7 (Bb, Db, F, G)
    (52, 2.5), (54, 2.5), (57, 2.5), (59, 2.5),
    # Bar 4: Eb7 (Eb, G, Bb, D)
    (50, 3.5), (55, 3.5), (52, 3.5), (58, 3.5),
    # Bar 4: Am7 (A, C, E, G)
    (57, 4.5), (59, 4.5), (61, 4.5), (62, 4.5)
]
for pitch, time in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5), (65, 1.75), (62, 2.0), (65, 2.25),  # Bar 2
    (62, 2.5), (65, 2.75), (62, 3.0), (65, 3.25),  # Bar 3
    (62, 3.5), (65, 3.75), (62, 4.0), (65, 4.25)   # Bar 4
]
for pitch, time in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
