
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

# Bass: Marcus. Walking line. Roots and fifths with chromatic approaches.
# F7: F, C, Ab, D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=90, pitch=73, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625), # G2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0), # A2 (F7)
    
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375), # A2
    pretty_midi.Note(velocity=90, pitch=75, start=3.375, end=3.75), # C3 (F7)
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.125), # Bb2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=73, start=4.125, end=4.5), # Ab2 (F7)
    
    pretty_midi.Note(velocity=90, pitch=73, start=4.5, end=4.875), # Ab2
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25), # D3 (F7)
    pretty_midi.Note(velocity=90, pitch=75, start=5.25, end=5.625), # C3 (chromatic)
    pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=6.0), # Bb2 (F7)
]
bass.notes.extend(bass_notes)

# Piano: Diane. Open voicings, different chord each bar, resolve on the last.
# Bar 2: F7 (F, A, C, Eb)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: E7 (E, G#, B, D)
piano_notes = [
    # Bar 2: F7
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # F3
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875), # A3
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875), # C4
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875), # Eb4
    
    # Bar 3: Bb7
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375), # Bb3
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375), # D4
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375), # F4
    pretty_midi.Note(velocity=100, pitch=75, start=3.0, end=3.375), # Ab4
    
    # Bar 4: E7
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # E3
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875), # G#3
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875), # B3
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # D4
]
piano.notes.extend(piano_notes)

# Sax: Dante. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Bb, A, F (F7)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75), # F3
    pretty_midi.Note(velocity=110, pitch=74, start=1.75, end=2.0), # Ab3
    pretty_midi.Note(velocity=110, pitch=73, start=2.0, end=2.25), # A3
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.5), # F3
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875), # F3 (return)
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)

drums.notes.extend([note for note in drum_notes if note.start >= 1.5])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
