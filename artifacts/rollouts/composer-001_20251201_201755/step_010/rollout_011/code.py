
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # A2
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),  # G2 (chromatic approach)
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75), # C3
    pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=4.125), # E3
    pretty_midi.Note(velocity=100, pitch=46, start=4.125, end=4.5),  # D3 (chromatic approach)
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=46, start=4.5, end=4.875),  # D3
    pretty_midi.Note(velocity=100, pitch=48, start=4.875, end=5.25), # E3
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625), # G3
    pretty_midi.Note(velocity=100, pitch=49, start=5.625, end=6.0),  # F#3 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last beat
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # C4 (Dmaj7)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # E4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # A4
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # D4 (D7)
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375),  # F#4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # C5
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # B3 (Dm7)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # A4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # B4 (Motif start)
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # D5 (Motif continuation)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # B4 (End of motif)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # D5 (Motif return)
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25), # E5 (Motif completion)
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # D5 (Motif resolution)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4 (1.5 - 6.0s)
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.0, end=start + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.1875, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.5625, end=start + 0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.9375, end=start + 1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.3125, end=start + 1.5)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
