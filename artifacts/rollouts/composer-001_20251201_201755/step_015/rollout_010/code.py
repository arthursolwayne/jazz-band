
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),   # hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),   # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875)    # hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),   # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),   # D2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),   # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),   # G4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),   # B4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),   # C#5
]
# Bar 3: G7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # C#5
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625),  # E5
    pretty_midi.Note(velocity=90, pitch=77, start=2.25, end=2.625),  # F#5
])
# Bar 4: C7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),   # C4
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),   # E4
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),   # B4
])
piano.notes.extend(piano_notes)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25), # F4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625), # D4
    pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=3.0),  # F4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),   # G2
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75),  # Ab2
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125),  # D2
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5),   # G2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: G7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),   # G4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),   # C#5
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),   # E5
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.375),   # F#5
]
# Bar 4: C7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75),   # C4
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),   # E4
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),   # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),   # B4
])
# Bar 4: End on D7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),   # D4
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),   # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),   # B4
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),   # C#5
])
piano.notes.extend(piano_notes)

# Dante: Motif continuation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # D4
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125), # F4
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),  # D4
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),   # hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),  # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5)    # hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),   # G2
    pretty_midi.Note(velocity=80, pitch=45, start=4.875, end=5.25),  # Bb2
    pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.625),  # D2
    pretty_midi.Note(velocity=80, pitch=43, start=5.625, end=6.0),   # G2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: D7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),   # D4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),   # G4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),   # B4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),   # C#5
]
piano.notes.extend(piano_notes)

# Dante: Motif conclusion
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=68, start=4.875, end=5.25), # F4
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625), # D4
    pretty_midi.Note(velocity=100, pitch=68, start=5.625, end=6.0),  # F4
]
sax.notes.extend(sax_notes)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),   # hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),  # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)    # hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
