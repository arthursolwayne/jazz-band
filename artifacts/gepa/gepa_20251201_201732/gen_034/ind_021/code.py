
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
    time = bar * 1.5
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 1.125)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.75)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 1.125, end=time + 1.5)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
for bar in range(2, 5):
    time = bar * 1.5
    # Bar 2: D2 - F2 (root and b3), chromatic approach from C2
    note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.375)
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=40, start=time + 0.375, end=time + 0.75)
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=41, start=time + 0.75, end=time + 1.125)
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=43, start=time + 1.125, end=time + 1.5)
    bass.notes.append(note)

    # Bar 3: G2 - Bb2 (fifth and root), chromatic approach from Ab2
    note = pretty_midi.Note(velocity=100, pitch=43, start=time + 1.5, end=time + 1.875)
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=44, start=time + 1.875, end=time + 2.25)
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=43, start=time + 2.25, end=time + 2.625)
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=41, start=time + 2.625, end=time + 3.0)
    bass.notes.append(note)

    # Bar 4: C2 - Eb2 (root of next chord), chromatic approach from Db2
    note = pretty_midi.Note(velocity=100, pitch=38, start=time + 3.0, end=time + 3.375)
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=40, start=time + 3.375, end=time + 3.75)
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=39, start=time + 3.75, end=time + 4.125)
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=40, start=time + 4.125, end=time + 4.5)
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
note = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.75)
piano.notes.append(note)

# Bar 3: Bb7 (Bb, D, F, Ab)
note = pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25)
piano.notes.append(note)

# Bar 4: Eb7 (Eb, G, Bb, Db)
note = pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75)
piano.notes.append(note)

# You: Tenor sax, one short motif, start it, leave it hanging, come back and finish it
# Bar 2: Motif starts at 1.5s with F (65), Ab (66), D (68), then leave it hanging
note = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=68, start=2.0, end=2.25)
sax.notes.append(note)

# Bar 4: Return to finish the motif
note = pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75)
sax.notes.append(note)

# Drums: Bars 2-4
for bar in range(2, 5):
    time = bar * 1.5
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 1.125)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.75)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 1.125, end=time + 1.5)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
