
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.05)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# BASS: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: Dm7 -> G7 -> Cm7 -> F7
bass_notes = [
    (38, 1.5),     # D2
    (40, 1.875),   # F2 (chromatic approach)
    (43, 2.25),    # G2
    (43, 2.625),   # G2
    (45, 2.625),   # Bb2 (chromatic approach)
    (48, 3.0),     # C3
    (50, 3.375),   # D3 (chromatic approach)
    (53, 3.75),    # E3
    (53, 4.125),   # E3
    (55, 4.125),   # F#3 (chromatic approach)
    (58, 4.5),     # G3
    (60, 4.875),   # A3 (chromatic approach)
    (63, 5.25),    # B3
    (63, 5.625),   # B3
    (65, 5.625),   # C#4 (chromatic approach)
    (68, 6.0)      # D4
]
for pitch, time in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.1)
    bass.notes.append(note)

# PIANO: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.1)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + 0.1)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.5 + 0.1)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.5 + 0.1)
piano.notes.append(note)

# Bar 3: G7 (G, B, D, F)
note = pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.25 + 0.1)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.25 + 0.1)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.25 + 0.1)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.25 + 0.1)
piano.notes.append(note)

# Bar 4: Cm7 (C, Eb, G, Bb)
note = pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.0 + 0.1)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.0 + 0.1)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.0 + 0.1)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.0 + 0.1)
piano.notes.append(note)

# SAX: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - F# - D - F#
# Start on bar 2, leave it hanging on F#, come back on bar 4 to finish it
note = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.5 + 0.2)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=66, start=1.5 + 0.375, end=1.5 + 0.375 + 0.2)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=3.75 + 0.2)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=66, start=4.125, end=4.125 + 0.2)
sax.notes.append(note)

# Drums: Bars 2-4
for bar in range(2, 4):
    start_time = bar * 1.5
    for beat in range(4):
        time = start_time + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.05)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
