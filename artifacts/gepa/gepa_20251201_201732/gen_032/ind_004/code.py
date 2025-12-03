
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
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),  # A2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # C4
]
piano.notes.extend(piano_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),  # F4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: G2 (MIDI 43) - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75), # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125), # A2
    pretty_midi.Note(velocity=90, pitch=47, start=4.125, end=4.5),  # Bb2
]
bass.notes.extend(bass_notes)

# Piano: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.25),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.125),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=3.125, end=3.25),  # D4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: A2 (MIDI 45) - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=4.5, end=4.875),  # A2
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25), # G2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=47, start=5.25, end=5.625), # Bb2
    pretty_midi.Note(velocity=90, pitch=49, start=5.625, end=6.0),  # C3
]
bass.notes.extend(bass_notes)

# Piano: Gm7 (G, Bb, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # F4
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.625, end=4.75),  # F4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drum_hihat = pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bar 3: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)
drum_hihat = pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bar 4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)
drum_hihat = pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
