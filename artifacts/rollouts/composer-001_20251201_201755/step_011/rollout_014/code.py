
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (D2-G2, roots and fifths with chromatic approaches)
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # D2
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75), # G2
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.125), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # D2
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25), # G2
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # D2
]
bass.notes.extend(bass_notes)

# Piano: Diane (open voicings, different chord each bar, resolve on the last)
piano_notes = []
# Bar 2 (1.5 - 3.0s) - Dm7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # F4
])
# Bar 3 (3.0 - 4.5s) - Bb7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # D5
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # F#5
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375), # C5
])
# Bar 4 (4.5 - 6.0s) - G7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # G4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # B4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875), # D5
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # F#4
])
piano.notes.extend(piano_notes)

# Sax: Dante (short motif, make it sing)
# Bar 2 (1.5 - 3.0s) - Motif: D4, F4, G4, F4 (start it, leave it hanging)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875), # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.6875, end=1.875), # F4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0625), # G4
    pretty_midi.Note(velocity=110, pitch=65, start=2.0625, end=2.25), # F4
    # Bar 3 (3.0 - 4.5s) - Repeat motif
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875), # D4
    pretty_midi.Note(velocity=110, pitch=65, start=3.1875, end=3.375), # F4
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.5625), # G4
    pretty_midi.Note(velocity=110, pitch=65, start=3.5625, end=3.75), # F4
    # Bar 4 (4.5 - 6.0s) - Finish it
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875), # D4
    pretty_midi.Note(velocity=110, pitch=65, start=4.6875, end=4.875), # F4
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.0625), # G4
    pretty_midi.Note(velocity=110, pitch=65, start=5.0625, end=5.25), # F4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.4375), # D4
    pretty_midi.Note(velocity=110, pitch=60, start=5.4375, end=5.625), # C4
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5)
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_intro.mid')
