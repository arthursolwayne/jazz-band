
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
bar_length = 1.5

# Kick on 1 and 3
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)

# Snare on 2 and 4
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0)

# Hihat on every eighth
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375)
drum_hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75)
drum_hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125)
drum_hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
drum_hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875)
drum_hihat6 = pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25)
drum_hihat7 = pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625)
drum_hihat8 = pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)

drums.notes.extend([drum_kick, drum_kick2, drum_snare, drum_snare2,
                    drum_hihat, drum_hihat2, drum_hihat3, drum_hihat4,
                    drum_hihat5, drum_hihat6, drum_hihat7, drum_hihat8])

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=100, pitch=39, start=2.625, end=3.0),  # Eb2
]

bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C4
]

piano.notes.extend(piano_notes)

# Sax: Motif, start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # C4
]

sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line
bass_notes2 = [
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.375),  # E2
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # D2
    pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.125),  # F2
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5),  # G2
]

bass.notes.extend(bass_notes2)

# Piano: Cm7 (C, Eb, G, Bb)
piano_notes2 = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # Bb4
]

piano.notes.extend(piano_notes2)

# Sax: Motif variation
sax_notes2 = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # C4
]

sax.notes.extend(sax_notes2)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line
bass_notes3 = [
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),  # G2
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25),  # E2
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # D2
    pretty_midi.Note(velocity=100, pitch=41, start=5.625, end=6.0),  # F2
]

bass.notes.extend(bass_notes3)

# Piano: G7 (G, B, D, F)
piano_notes3 = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F4
]

piano.notes.extend(piano_notes3)

# Sax: Finish the motif
sax_notes3 = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # C4
]

sax.notes.extend(sax_notes3)

# Drums: Bar 3 and 4
# Bar 3: Kick on 1 and 3
drum_kick3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_kick4 = pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)

# Snare on 2 and 4
drum_snare3 = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875)
drum_snare4 = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0)

# Hihat on every eighth
drum_hihat9 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375)
drum_hihat10 = pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75)
drum_hihat11 = pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125)
drum_hihat12 = pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5)
drum_hihat13 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875)
drum_hihat14 = pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25)
drum_hihat15 = pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625)
drum_hihat16 = pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)

drums.notes.extend([drum_kick3, drum_kick4, drum_snare3, drum_snare4,
                    drum_hihat9, drum_hihat10, drum_hihat11, drum_hihat12,
                    drum_hihat13, drum_hihat14, drum_hihat15, drum_hihat16])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
