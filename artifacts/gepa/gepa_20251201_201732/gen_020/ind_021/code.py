
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

# Kick on 1 and 3
drum_kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_kick_2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.extend([drum_kick_1, drum_kick_2])

# Snare on 2 and 4
drum_snare_1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875)
drum_snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0)
drums.notes.extend([drum_snare_1, drum_snare_2])

# Hi-hat on every eighth
for i in range(0, 6, 1):
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=i * 0.375, end=(i + 1) * 0.375)
    drums.notes.append(hihat)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43)
# D2 (38), Eb2 (39), F2 (41), G2 (43), Ab2 (44), Bb2 (45), B2 (46), C3 (48), D3 (50)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75),  # D2
    pretty_midi.Note(velocity=100, pitch=39, start=1.75, end=2.0),  # Eb2
    pretty_midi.Note(velocity=100, pitch=41, start=2.0, end=2.25),  # F2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.5),  # G2
    pretty_midi.Note(velocity=100, pitch=44, start=2.5, end=2.75),  # Ab2
    pretty_midi.Note(velocity=100, pitch=45, start=2.75, end=3.0),  # Bb2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, G)
# Bar 3: Gm7 (Bb, D, G, B)
# Bar 4: C7 (E, G, C, Bb)
# Comp on 2 and 4
piano_notes = [
    # Dm7 (F, A, D, G) on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=2.0, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G4
    # Gm7 (Bb, D, G, B) on beat 4
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.25),  # Bb4
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # B4
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5 - 3.0s
for i in range(0, 4, 1):
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=1.5 + i * 0.375, end=1.5 + (i + 1) * 0.375)
    drums.notes.append(hihat)

drum_kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_kick_4 = pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0)
drums.notes.extend([drum_kick_3, drum_kick_4])

drum_snare_3 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0)
drum_snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125)
drums.notes.extend([drum_snare_3, drum_snare_4])

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking bass line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=46, start=3.0, end=3.25),  # B2
    pretty_midi.Note(velocity=100, pitch=48, start=3.25, end=3.5),  # C3
    pretty_midi.Note(velocity=100, pitch=50, start=3.5, end=3.75),  # D3
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.0),  # G2
    pretty_midi.Note(velocity=100, pitch=44, start=4.0, end=4.25),  # Ab2
    pretty_midi.Note(velocity=100, pitch=45, start=4.25, end=4.5),  # Bb2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: C7 (E, G, C, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),  # C4
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.25),  # Bb4
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 3: 3.0 - 4.5s
for i in range(0, 4, 1):
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=3.0 + i * 0.375, end=3.0 + (i + 1) * 0.375)
    drums.notes.append(hihat)

drum_kick_5 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_kick_6 = pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)
drums.notes.extend([drum_kick_5, drum_kick_6])

drum_snare_5 = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5)
drum_snare_6 = pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625)
drums.notes.extend([drum_snare_5, drum_snare_6])

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking bass line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.75),  # D3
    pretty_midi.Note(velocity=100, pitch=43, start=4.75, end=5.0),  # G2
    pretty_midi.Note(velocity=100, pitch=44, start=5.0, end=5.25),  # Ab2
    pretty_midi.Note(velocity=100, pitch=45, start=5.25, end=5.5),  # Bb2
    pretty_midi.Note(velocity=100, pitch=46, start=5.5, end=5.75),  # B2
    pretty_midi.Note(velocity=100, pitch=48, start=5.75, end=6.0),  # C3
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: Dm7 (F, A, D, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.75),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # G4
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 4: 4.5 - 6.0s
for i in range(0, 4, 1):
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=4.5 + i * 0.375, end=4.5 + (i + 1) * 0.375)
    drums.notes.append(hihat)

drum_kick_7 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_kick_8 = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)
drums.notes.extend([drum_kick_7, drum_kick_8])

drum_snare_7 = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0)
drum_snare_8 = pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125)
drums.notes.extend([drum_snare_7, drum_snare_8])

# Sax: Your moment (Bar 2-4)
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Motif: Dm scale, but not scales — a phrase
# D4 (62), F4 (65), Eb4 (64), D4 (62), C4 (60), Bb4 (61), G4 (67), D4 (62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=1.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=2.375, end=2.5),  # C4
    pretty_midi.Note(velocity=100, pitch=61, start=2.5, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.75),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # D4
]
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
# midi.write disabled
