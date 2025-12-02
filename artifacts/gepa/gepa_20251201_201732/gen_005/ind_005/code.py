
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
    start = bar * 1.5
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Fm (F2, Bb2, Ab2, D2, G2, C2, Eb2, etc.)
# Roots and fifths with chromatic approaches
for bar in range(2, 5):
    start = bar * 1.5
    # Bar 2: Fm (F2, C2) with chromatic approach
    note = pretty_midi.Note(velocity=100, pitch=71, start=start, end=start + 0.375)  # F2
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=67, start=start + 0.25, end=start + 0.625)  # Eb2
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=69, start=start + 0.5, end=start + 0.875)  # F2
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=67, start=start + 0.75, end=start + 1.125)  # Eb2
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=69, start=start + 1.0, end=start + 1.375)  # F2
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=67, start=start + 1.25, end=start + 1.625)  # Eb2
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=69, start=start + 1.5, end=start + 1.875)  # F2
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7
note = pretty_midi.Note(velocity=100, pitch=64, start=start, end=start + 0.75)  # F
note2 = pretty_midi.Note(velocity=100, pitch=69, start=start, end=start + 0.75)  # C
note3 = pretty_midi.Note(velocity=100, pitch=71, start=start, end=start + 0.75)  # Eb
note4 = pretty_midi.Note(velocity=100, pitch=76, start=start, end=start + 0.75)  # Ab
piano.notes.append(note)
piano.notes.append(note2)
piano.notes.append(note3)
piano.notes.append(note4)

# Bar 3: Bb7
note = pretty_midi.Note(velocity=100, pitch=62, start=start + 1.5, end=start + 2.25)  # Bb
note2 = pretty_midi.Note(velocity=100, pitch=67, start=start + 1.5, end=start + 2.25)  # F
note3 = pretty_midi.Note(velocity=100, pitch=71, start=start + 1.5, end=start + 2.25)  # Ab
note4 = pretty_midi.Note(velocity=100, pitch=76, start=start + 1.5, end=start + 2.25)  # Db
piano.notes.append(note)
piano.notes.append(note2)
piano.notes.append(note3)
piano.notes.append(note4)

# Bar 4: Cm7
note = pretty_midi.Note(velocity=100, pitch=60, start=start + 3.0, end=start + 3.75)  # C
note2 = pretty_midi.Note(velocity=100, pitch=65, start=start + 3.0, end=start + 3.75)  # G
note3 = pretty_midi.Note(velocity=100, pitch=67, start=start + 3.0, end=start + 3.75)  # Ab
note4 = pretty_midi.Note(velocity=100, pitch=72, start=start + 3.0, end=start + 3.75)  # Db
piano.notes.append(note)
piano.notes.append(note2)
piano.notes.append(note3)
piano.notes.append(note4)

# You: Tenor sax — one short motif, sing it, leave it hanging
# Bar 2: Start the motif
note = pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875)  # F4
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25)  # C4
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625)  # Eb4
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0)  # F4
sax.notes.append(note)

# Bar 3: Continue the motif
note = pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375)  # F4
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75)  # C4
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.125)  # Eb4
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5)  # F4
sax.notes.append(note)

# Bar 4: Finish the motif
note = pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875)  # F4
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25)  # C4
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625)  # Eb4
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0)  # F4
sax.notes.append(note)

# Drums: Bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
