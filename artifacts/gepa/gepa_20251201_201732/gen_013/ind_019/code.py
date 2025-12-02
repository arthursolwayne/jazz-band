
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
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=80, pitch=76, start=1.875, end=2.25), # C3 (fifth)
    pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.625),  # B (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),  # F2 (root)
    pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=3.375),  # C3 (fifth)
    pretty_midi.Note(velocity=80, pitch=78, start=3.375, end=3.75), # D (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=76, start=3.75, end=4.125), # C3 (fifth)
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5),  # F2 (root)
    pretty_midi.Note(velocity=80, pitch=76, start=4.5, end=4.875),  # C3 (fifth)
    pretty_midi.Note(velocity=80, pitch=74, start=4.875, end=5.25), # B (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625), # F2 (root)
    pretty_midi.Note(velocity=80, pitch=76, start=5.625, end=6.0),  # C3 (fifth)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on last chord
# Bar 2: Fmaj7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.25), # F4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=2.25), # A4
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=2.25), # C5
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=2.25), # E5
]
# Bar 3: Bm7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=3.0), # B4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=3.0), # D5
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=3.0), # F#5
    pretty_midi.Note(velocity=90, pitch=78, start=2.25, end=3.0), # A5
])
# Bar 4: Fmaj7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.75), # F4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.75), # A4
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.75), # C5
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.75), # E5
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F4 - A4 - F4 - G4 (sus4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G4 (sus4)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # F4 (return)
    pretty_midi.Note(velocity=100, pitch=68, start=3.25, end=3.5),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # G4 (sus4)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=4.75, end=5.0),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # G4 (sus4)
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=5.75, end=6.0),  # A4
]
sax.notes.extend(sax_notes)

# Drums: Continue with hihat on every eighth, kick on 1 and 3, snare on 2 and 4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    hihat1 = pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125)
    # Kick on 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=start + 1.5, end=start + 1.875)
    # Add to drums
    drums.notes.extend([kick, hihat1, snare, hihat2, kick, hihat3, snare, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
