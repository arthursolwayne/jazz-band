
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line (D2-G2, MIDI 38-43), roots and fifths, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Fm root
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # Bb (fifth)
    pretty_midi.Note(velocity=100, pitch=37, start=2.25, end=2.625), # Eb (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),  # Ab (third)
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # C (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Fm root
    pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.125), # Bb (fifth)
    pretty_midi.Note(velocity=100, pitch=39, start=4.125, end=4.5),  # G (chromatic approach)
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.875),  # Ab (third)
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Fm root
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625), # Bb (fifth)
    pretty_midi.Note(velocity=100, pitch=37, start=5.625, end=6.0),  # Eb (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F Ab C Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=1.875),  # Eb
    
    # Bar 3: Bb7 (Bb D F Ab)
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # Ab
    
    # Bar 4: Eb7 (Eb G Bb D)
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # G
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),  # F
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # Bb
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    kick_start = bar_start + 0.0
    snare_start = bar_start + 0.375
    kick_start2 = bar_start + 0.75
    snare_start2 = bar_start + 1.125
    hihat_start = bar_start
    for i in range(0, 4):
        hihat_start += 0.375
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_start + 0.375)
        drums.notes.append(hihat)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=kick_start2, end=kick_start2 + 0.375)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=snare_start2, end=snare_start2 + 0.375)
    drums.notes.extend([kick, snare, kick2, snare2])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
