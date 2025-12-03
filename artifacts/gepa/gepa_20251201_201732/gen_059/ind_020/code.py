
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
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2, F#2, G2, A2
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=40, start=1.5 + 0.375, end=1.5 + 0.75),
    pretty_midi.Note(velocity=100, pitch=43, start=1.5 + 0.75, end=1.5 + 1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5 + 1.125, end=1.5 + 1.5),
    
    # Bar 3: A2, B2, C#3, D3
    pretty_midi.Note(velocity=100, pitch=42, start=1.5 + 1.5, end=1.5 + 1.875),
    pretty_midi.Note(velocity=100, pitch=43, start=1.5 + 1.875, end=1.5 + 2.25),
    pretty_midi.Note(velocity=100, pitch=45, start=1.5 + 2.25, end=1.5 + 2.625),
    pretty_midi.Note(velocity=100, pitch=47, start=1.5 + 2.625, end=1.5 + 3.0),
    
    # Bar 4: D3, F#2, G2, A2
    pretty_midi.Note(velocity=100, pitch=47, start=1.5 + 3.0, end=1.5 + 3.375),
    pretty_midi.Note(velocity=100, pitch=40, start=1.5 + 3.375, end=1.5 + 3.75),
    pretty_midi.Note(velocity=100, pitch=43, start=1.5 + 3.75, end=1.5 + 4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5 + 4.125, end=1.5 + 4.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.5 + 0.375),
]
piano.notes.extend(piano_notes)

# Bar 3: F#7 (F#-A#-C#-E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=51, start=1.5 + 1.5, end=1.5 + 1.875),
    pretty_midi.Note(velocity=100, pitch=54, start=1.5 + 1.5, end=1.5 + 1.875),
    pretty_midi.Note(velocity=100, pitch=56, start=1.5 + 1.5, end=1.5 + 1.875),
    pretty_midi.Note(velocity=100, pitch=58, start=1.5 + 1.5, end=1.5 + 1.875),
]
piano.notes.extend(piano_notes)

# Bar 4: G7 (G-B-D-F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=1.5 + 3.0, end=1.5 + 3.375),
    pretty_midi.Note(velocity=100, pitch=57, start=1.5 + 3.0, end=1.5 + 3.375),
    pretty_midi.Note(velocity=100, pitch=59, start=1.5 + 3.0, end=1.5 + 3.375),
    pretty_midi.Note(velocity=100, pitch=61, start=1.5 + 3.0, end=1.5 + 3.375),
]
piano.notes.extend(piano_notes)

# Drums: continue the pattern
for bar in range(2, 4):
    for beat in range(4):
        time = 1.5 + bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (50) - F# (53) - G (55) - D (50)
# Play first two notes in bar 2, finish in bar 4

# Bar 2: D (50), F# (53)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=50, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=110, pitch=53, start=1.5 + 0.375, end=1.5 + 0.75),
]

# Bar 3: rest
# Bar 4: G (55), D (50)
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=55, start=1.5 + 3.0, end=1.5 + 3.375),
    pretty_midi.Note(velocity=110, pitch=50, start=1.5 + 3.375, end=1.5 + 3.75),
])
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
