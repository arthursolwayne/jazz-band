
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
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus on walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # A2
    pretty_midi.Note(velocity=100, pitch=39, start=2.625, end=3.0),  # Eb2 (chromatic approach)
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75), # B2
    pretty_midi.Note(velocity=100, pitch=47, start=3.75, end=4.125), # D3
    pretty_midi.Note(velocity=100, pitch=44, start=4.125, end=4.5),  # C3 (chromatic approach)
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # A2
    pretty_midi.Note(velocity=100, pitch=39, start=5.625, end=6.0),  # Eb2 (chromatic approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane on open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (1.5 - 3.0s) - D7sus4
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # C5
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # F5
    
    # Bar 3 (3.0 - 4.5s) - Bm7
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),  # B3
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # E4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # D5
    
    # Bar 4 (4.5 - 6.0s) - G13
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0),  # G3
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=6.0),  # B3
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # A4
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante on tenor, one short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2 (1.5 - 3.0s) - Start the motif
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # E4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # D4
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # C4
    
    # Bar 3 (3.0 - 4.5s) - Leave it hanging
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # D4
    
    # Bar 4 (4.5 - 6.0s) - Come back and finish it
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # D4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # E4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on every eighth
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + 1.5))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
