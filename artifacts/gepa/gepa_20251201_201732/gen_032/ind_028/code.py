
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
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: walking line (D2-G2), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root), F#2 (fifth), G2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=80, pitch=41, start=1.5 + 0.375, end=1.5 + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5 + 0.75, end=1.5 + 1.125),
    # Bar 3: A2 (fifth), C#2 (root), B2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=45, start=1.5 + 1.5, end=1.5 + 1.875),
    pretty_midi.Note(velocity=80, pitch=39, start=1.5 + 1.875, end=1.5 + 2.25),
    pretty_midi.Note(velocity=80, pitch=43, start=1.5 + 2.25, end=1.5 + 2.625),
    # Bar 4: D2 (root), F#2 (fifth), G2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5 + 3.0, end=1.5 + 3.375),
    pretty_midi.Note(velocity=80, pitch=41, start=1.5 + 3.375, end=1.5 + 3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5 + 3.75, end=1.5 + 4.125),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: A7 (D, A, C#, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.5 + 1.5),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.5 + 1.5),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.5 + 1.5),
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.5 + 1.5),
]
# Bar 3: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=1.5 + 1.5, end=1.5 + 3.0),
    pretty_midi.Note(velocity=90, pitch=63, start=1.5 + 1.5, end=1.5 + 3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5 + 1.5, end=1.5 + 3.0),
    pretty_midi.Note(velocity=90, pitch=62, start=1.5 + 1.5, end=1.5 + 3.0),
])
# Bar 4: D7 (D, F#, A, C#)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=1.5 + 3.0, end=1.5 + 4.5),
    pretty_midi.Note(velocity=90, pitch=66, start=1.5 + 3.0, end=1.5 + 4.5),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5 + 3.0, end=1.5 + 4.5),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5 + 3.0, end=1.5 + 4.5),
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62) - F# (66) - D (62) - E (65) - D (62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.375),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.5 + 0.375, end=1.5 + 0.75),  # F#
    pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 0.75, end=1.5 + 1.125),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.5 + 1.125, end=1.5 + 1.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 3.0, end=1.5 + 3.375),  # D
]
sax.notes.extend(sax_notes)

# Drums continue
for bar in range(2, 4):
    for beat in range(4):
        time = 1.5 + bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
