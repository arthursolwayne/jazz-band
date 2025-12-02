
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
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),   # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),   # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875), # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Eb2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0), # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Dm7 -> G7 -> Cm7 -> F7
piano_notes = [
    # Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),
    
    # G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),
    
    # Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=65, start=2.75, end=3.0),
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.75),   # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.125), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0),   # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.5),   # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.875), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.75), # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.125),  # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.625), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.5),  # Hihat
]
drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),    # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),    # E4
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),    # D4
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),    # C4
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),    # D4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_intro.mid')
