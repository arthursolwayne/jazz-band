
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=1.5),   # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.5),    # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),   # Hihat
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (MIDI 53) -> Bb2 (MIDI 57) -> Ab2 (MIDI 56) -> D2 (MIDI 50)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=100, pitch=57, start=1.875, end=2.25), # Bb2
    pretty_midi.Note(velocity=100, pitch=56, start=2.25, end=2.625), # Ab2
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0), # D2
]
bass.notes.extend(bass_notes)

# Piano: Fm7 -> Bb7 -> Ab7 -> D7 (open voicings, resolve on 4th beat)
piano_notes = [
    # Fm7: F, Ab, C, D (MIDI 53, 56, 57, 58)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=56, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=3.0),
    
    # Bb7: Bb, D, F, Ab (MIDI 57, 58, 53, 56)
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=56, start=1.5, end=3.0),
    
    # Ab7: Ab, C, Eb, Gb (MIDI 56, 57, 59, 60)
    pretty_midi.Note(velocity=100, pitch=56, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),
    
    # D7: D, F#, A, C (MIDI 50, 55, 57, 58)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=3.0),
]
piano.notes.extend(piano_notes)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0),     # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=3.0),   # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=3.0),    # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),   # Hihat
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: F2 (MIDI 53) -> Bb2 (MIDI 57) -> Ab2 (MIDI 56) -> D2 (MIDI 50)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375), # F2
    pretty_midi.Note(velocity=100, pitch=57, start=3.375, end=3.75), # Bb2
    pretty_midi.Note(velocity=100, pitch=56, start=3.75, end=4.125), # Ab2
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5), # D2
]
bass.notes.extend(bass_notes)

# Piano: Fm7 -> Bb7 -> Ab7 -> D7 (open voicings, resolve on 4th beat)
piano_notes = [
    # Fm7: F, Ab, C, D (MIDI 53, 56, 57, 58)
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=56, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=4.5),
    
    # Bb7: Bb, D, F, Ab (MIDI 57, 58, 53, 56)
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=56, start=3.0, end=4.5),
    
    # Ab7: Ab, C, Eb, Gb (MIDI 56, 57, 59, 60)
    pretty_midi.Note(velocity=100, pitch=56, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),
    
    # D7: D, F#, A, C (MIDI 50, 55, 57, 58)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=4.5),
]
piano.notes.extend(piano_notes)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5),     # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=4.5),   # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.5),    # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),   # Hihat
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: F2 (MIDI 53) -> Bb2 (MIDI 57) -> Ab2 (MIDI 56) -> D2 (MIDI 50)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875), # F2
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25), # Bb2
    pretty_midi.Note(velocity=100, pitch=56, start=5.25, end=5.625), # Ab2
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0), # D2
]
bass.notes.extend(bass_notes)

# Piano: Fm7 -> Bb7 -> Ab7 -> D7 (open voicings, resolve on 4th beat)
piano_notes = [
    # Fm7: F, Ab, C, D (MIDI 53, 56, 57, 58)
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=6.0),
    
    # Bb7: Bb, D, F, Ab (MIDI 57, 58, 53, 56)
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=6.0),
    
    # Ab7: Ab, C, Eb, Gb (MIDI 56, 57, 59, 60)
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),
    
    # D7: D, F#, A, C (MIDI 50, 55, 57, 58)
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=6.0),
]
piano.notes.extend(piano_notes)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0),     # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=6.0),   # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=6.0),    # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),   # Hihat
]
drums.notes.extend(drum_notes)

# Saxophone: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, C, Db
# Motif: F -> Ab -> Bb -> C (MIDI 53, 56, 57, 58)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=110, pitch=56, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=110, pitch=57, start=2.625, end=3.0), # Bb
    pretty_midi.Note(velocity=110, pitch=58, start=3.0, end=3.375), # C
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=110, pitch=56, start=5.25, end=5.625), # Ab
    pretty_midi.Note(velocity=110, pitch=57, start=5.625, end=6.0), # Bb
    pretty_midi.Note(velocity=110, pitch=58, start=6.0, end=6.375), # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
