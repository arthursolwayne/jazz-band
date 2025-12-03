
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)   # Hihat
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # F2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # Dmaj7 (D, F#, A, C#)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # Em7 (E, G, B, D)
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),
    
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # Gmaj7 (G, B, D, F#)
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=77, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0)
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875), # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25), # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)   # Hihat
]
drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75), # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # B4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # B4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
