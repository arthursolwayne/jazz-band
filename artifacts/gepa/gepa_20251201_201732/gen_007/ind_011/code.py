
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    drums.notes.append(snare)
    # Kick on 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    drums.notes.append(kick)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: Dm7 - D (38), F (41), A (45), C (48)
# Chromatic approach: C# (43) to D (38)
bass_note = pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.5 + 0.375)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=38, start=1.5 + 0.375, end=1.5 + 0.75)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=41, start=1.5 + 0.75, end=1.5 + 1.125)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=45, start=1.5 + 1.125, end=1.5 + 1.5)
bass.notes.append(bass_note)

# Bar 3: Gm7 - G (43), Bb (46), D (49), F (52)
# Chromatic approach: F# (51) to G (43)
bass_note = pretty_midi.Note(velocity=100, pitch=51, start=1.5 + 1.5, end=1.5 + 1.875)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=43, start=1.5 + 1.875, end=1.5 + 2.25)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=46, start=1.5 + 2.25, end=1.5 + 2.625)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=49, start=1.5 + 2.625, end=1.5 + 3.0)
bass.notes.append(bass_note)

# Bar 4: Cm7 - C (40), Eb (44), G (48), Bb (50)
# Chromatic approach: B (48) to C (40)
bass_note = pretty_midi.Note(velocity=100, pitch=48, start=1.5 + 3.0, end=1.5 + 3.375)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=40, start=1.5 + 3.375, end=1.5 + 3.75)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=44, start=1.5 + 3.75, end=1.5 + 4.125)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=48, start=1.5 + 4.125, end=1.5 + 4.5)
bass.notes.append(bass_note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
note = pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.5 + 0.75)  # D
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.5 + 0.75)  # F
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.5 + 0.75)  # A
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.5 + 0.75)  # C
piano.notes.append(note)

# Bar 3: Gm7 (G, Bb, D, F)
note = pretty_midi.Note(velocity=90, pitch=67, start=1.5 + 1.5, end=1.5 + 2.25)  # G
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=69, start=1.5 + 1.5, end=1.5 + 2.25)  # Bb
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=72, start=1.5 + 1.5, end=1.5 + 2.25)  # D
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=71, start=1.5 + 1.5, end=1.5 + 2.25)  # F
piano.notes.append(note)

# Bar 4: Cm7 (C, Eb, G, Bb)
note = pretty_midi.Note(velocity=90, pitch=60, start=1.5 + 3.0, end=1.5 + 3.75)  # C
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=63, start=1.5 + 3.0, end=1.5 + 3.75)  # Eb
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=1.5 + 3.0, end=1.5 + 3.75)  # G
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=69, start=1.5 + 3.0, end=1.5 + 3.75)  # Bb
piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F (65), Bb (69), D (62) — but spread out across bars 2-4
# Bar 2: D (62) on beat 2
note = pretty_midi.Note(velocity=110, pitch=62, start=1.5 + 0.75, end=1.5 + 1.125)
sax.notes.append(note)

# Bar 3: F (65) on beat 2, Bb (69) on beat 3
note = pretty_midi.Note(velocity=110, pitch=65, start=1.5 + 2.25, end=1.5 + 2.625)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=69, start=1.5 + 2.625, end=1.5 + 3.0)
sax.notes.append(note)

# Bar 4: D (62) on beat 2, and then D (62) on beat 3
note = pretty_midi.Note(velocity=110, pitch=62, start=1.5 + 3.75, end=1.5 + 4.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=62, start=1.5 + 4.125, end=1.5 + 4.5)
sax.notes.append(note)

# Drums continue in bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    drums.notes.append(snare)
    # Kick on 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    drums.notes.append(kick)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
