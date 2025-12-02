
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
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5, program=42)
drum_hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0, program=42)
drum_hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5, program=42)
drum_hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0, program=42)
drums.notes.extend([drum_kick, drum_kick2, drum_snare, drum_snare2,
                    drum_hihat, drum_hihat2, drum_hihat3, drum_hihat4])

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line (D2-G2, roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),  # A2 (fifth of D)
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # G2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano comp (open voicings, different chord each bar, resolve on the last)
piano_notes = [
    # Bar 2: Dmaj7 (D-F#-A-C#)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C#4
    # Bar 3: Bm7 (B-D-F#-A)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # A4
    # Bar 4: G7 (G-B-D-F)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # F4
]
piano.notes.extend(piano_notes)

# Saxophone motif: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start the motif (D4 - F#4 - A4 - G4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625),  # A4
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),  # G4
    # Bar 3: Leave it hanging, rest
    # Bar 4: Come back and finish the motif (D4 - A4 - G4 - D4)
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.25),  # A4
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.625),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),  # D4
]
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
