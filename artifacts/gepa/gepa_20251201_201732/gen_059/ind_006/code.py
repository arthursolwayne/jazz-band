
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
    time = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.75, end=time + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38) -> F2 (41) chromatic approach
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=40, start=1.5 + 0.375, end=1.5 + 0.75),
    pretty_midi.Note(velocity=100, pitch=41, start=1.5 + 0.75, end=1.5 + 1.125),
    pretty_midi.Note(velocity=100, pitch=43, start=1.5 + 1.125, end=1.5 + 1.5),
    # Bar 3: G2 (43) -> Bb2 (45) chromatic approach
    pretty_midi.Note(velocity=100, pitch=43, start=1.5 + 1.5, end=1.5 + 1.875),
    pretty_midi.Note(velocity=100, pitch=44, start=1.5 + 1.875, end=1.5 + 2.25),
    pretty_midi.Note(velocity=100, pitch=45, start=1.5 + 2.25, end=1.5 + 2.625),
    pretty_midi.Note(velocity=100, pitch=47, start=1.5 + 2.625, end=1.5 + 3.0),
    # Bar 4: D2 (38) -> F2 (41) chromatic approach
    pretty_midi.Note(velocity=100, pitch=38, start=1.5 + 3.0, end=1.5 + 3.375),
    pretty_midi.Note(velocity=100, pitch=40, start=1.5 + 3.375, end=1.5 + 3.75),
    pretty_midi.Note(velocity=100, pitch=41, start=1.5 + 3.75, end=1.5 + 4.125),
    pretty_midi.Note(velocity=100, pitch=43, start=1.5 + 4.125, end=1.5 + 4.5),
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, G)
diane_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.5 + 0.75),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.5 + 0.75),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.75),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.5 + 0.75),  # G4
]
# Bar 3: G7 (B, D, G, F)
diane_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 1.5, end=1.5 + 2.25),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 1.5, end=1.5 + 2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 1.5, end=1.5 + 2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5 + 1.5, end=1.5 + 2.25),  # F4
]
# Bar 4: Cm7 (Eb, G, C, F)
diane_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=63, start=1.5 + 3.0, end=1.5 + 3.75),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 3.0, end=1.5 + 3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5 + 3.0, end=1.5 + 3.75),  # C4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5 + 3.0, end=1.5 + 3.75),  # F4
]
piano.notes.extend(diane_notes_bar2 + diane_notes_bar3 + diane_notes_bar4)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    time = 1.5 + (bar - 2) * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.75, end=time + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs
# Motif: D4 (62), F4 (65), G4 (67), D4 (62)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=110, pitch=65, start=1.5 + 0.375, end=1.5 + 0.75),
    pretty_midi.Note(velocity=110, pitch=67, start=1.5 + 0.75, end=1.5 + 1.125),
    pretty_midi.Note(velocity=110, pitch=62, start=1.5 + 2.25, end=1.5 + 2.625),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
