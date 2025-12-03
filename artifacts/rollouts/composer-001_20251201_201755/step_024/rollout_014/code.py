
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
drum_snare = pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (D2-G2, MIDI 38-43), walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=90, pitch=39, start=2.25, end=2.625), # F#2
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=85, pitch=72, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=80, pitch=74, start=1.5, end=3.0),  # E
]
piano.notes.extend(piano_notes)

# Sax: Motif starts here, one short phrase that sings
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=105, pitch=71, start=1.875, end=2.25), # B
    pretty_midi.Note(velocity=105, pitch=69, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=105, pitch=67, start=2.625, end=3.0),  # G
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: F2 again but with different chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75), # G2
    pretty_midi.Note(velocity=90, pitch=37, start=3.75, end=4.125), # E2
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # F2
]
bass.notes.extend(bass_notes)

# Piano: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=60, start=3.0, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=4.5),  # Eb
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=4.5),  # G
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=4.5),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=105, pitch=64, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=105, pitch=62, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=105, pitch=60, start=4.125, end=4.5),  # F
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: F2 again, resolving
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25), # G2
    pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625), # F2
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano: Fmaj7 again, resolving
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=71, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=6.0),  # A
    pretty_midi.Note(velocity=85, pitch=72, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=6.0),  # E
]
piano.notes.extend(piano_notes)

# Sax: Return to the motif, finish it
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=105, pitch=71, start=4.875, end=5.25), # B
    pretty_midi.Note(velocity=105, pitch=69, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=105, pitch=67, start=5.625, end=6.0),  # G
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Bar 3
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_snare = pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=4.125)
drum_hihat = pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bar 4
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_snare = pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.625)
drum_hihat = pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
