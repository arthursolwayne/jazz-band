
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
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625), # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # D2
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=90, pitch=47, start=3.375, end=3.75), # B2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125), # G2
    pretty_midi.Note(velocity=90, pitch=47, start=4.125, end=4.5),  # B2
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # D3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25),  # G2
    pretty_midi.Note(velocity=90, pitch=47, start=5.25, end=5.625),  # B2
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0)   # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C4 (octave lower)
]

# Bar 3: G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # F4 (octave lower)
])

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Bb4 (octave lower)
])

# Bar 4 resolution chord - Dm7 again
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # C4 (octave lower)
])

piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

# Saxophone: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F4 - G4 - D4 (saxophone part)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=1.875), # F4
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.125),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=2.125, end=2.3125), # D4
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),  # D4 (return)
    pretty_midi.Note(velocity=110, pitch=67, start=3.1875, end=3.375), # F4
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.625),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=3.625, end=3.8125), # D4
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.6875),  # C4 (chromatic approach)
    pretty_midi.Note(velocity=110, pitch=62, start=4.6875, end=4.875), # D4
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.0625), # F4
    pretty_midi.Note(velocity=110, pitch=69, start=5.0625, end=5.25),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.4375),  # D4
    pretty_midi.Note(velocity=110, pitch=62, start=5.4375, end=5.625), # D4 (hold)
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=5.8125), # D4
    pretty_midi.Note(velocity=110, pitch=62, start=5.8125, end=6.0)   # D4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
