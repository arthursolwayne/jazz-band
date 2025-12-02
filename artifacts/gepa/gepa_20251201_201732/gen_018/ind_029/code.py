
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
drum_pattern = [
    [36, 42],  # Kick on 1, hihat on 1
    [42],      # Hihat on 2
    [36, 42],  # Kick on 3, hihat on 3
    [38, 42]   # Snare on 4, hihat on 4
]
for i, notes in enumerate(drum_pattern):
    note = pretty_midi.Note(velocity=100, pitch=notes[0], start=i * 0.375, end=(i + 1) * 0.375)
    drums.notes.append(note)
    if len(notes) > 1:
        note = pretty_midi.Note(velocity=80, pitch=notes[1], start=i * 0.375, end=(i + 1) * 0.375)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    [38],          # D2 - root
    [41, 40],      # F2 - chromatic approach
    [43],          # A2 - fifth
    [42, 43],      # G2 - chromatic approach
    [38],          # D2 - root
    [41, 40],      # F2 - chromatic approach
    [43],          # A2 - fifth
    [42, 43],      # G2 - chromatic approach
    [38],          # D2 - root
    [41, 40],      # F2 - chromatic approach
    [43],          # A2 - fifth
    [42, 43]       # G2 - chromatic approach
]
for i, note in enumerate(bass_notes):
    if isinstance(note, list):
        for pitch in note:
            n = pretty_midi.Note(velocity=80, pitch=pitch, start=(i * 0.375) + 1.5, end=(i + 1) * 0.375 + 1.5)
            bass.notes.append(n)
    else:
        n = pretty_midi.Note(velocity=80, pitch=note, start=(i * 0.375) + 1.5, end=(i + 1) * 0.375 + 1.5)
        bass.notes.append(n)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    [50, 52, 55, 57],  # Dm7
    [50, 52, 55, 57],  # Dm7
    [50, 52, 55, 57],  # Dm7
    [50, 52, 55, 57],  # Dm7
    [50, 52, 55, 57],  # Dm7
    [50, 52, 55, 57],  # Dm7
    [50, 52, 55, 57],  # Dm7
    [50, 52, 55, 57],  # Dm7
    [50, 52, 55, 57],  # Dm7
    [50, 52, 55, 57],  # Dm7
    [50, 52, 55, 57],  # Dm7
    [50, 52, 55, 57]   # Dm7
]
for i, note in enumerate(piano_notes):
    for pitch in note:
        n = pretty_midi.Note(velocity=100, pitch=pitch, start=(i * 0.375) + 1.5, end=(i + 1) * 0.375 + 1.5)
        piano.notes.append(n)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7: D F A C (50,52,55,57)
# Motif: D, F, A, rest
sax_notes = [
    [50],            # D
    [52],            # F
    [55],            # A
    [],              # Rest
    [50],            # D
    [52],            # F
    [55],            # A
    [],              # Rest
    [50],            # D
    [52],            # F
    [55],            # A
    []               # Rest
]
for i, note in enumerate(sax_notes):
    if note:
        n = pretty_midi.Note(velocity=100, pitch=note[0], start=(i * 0.375) + 1.5, end=(i + 1) * 0.375 + 1.5)
        sax.notes.append(n)

# Drums: Bar 2-4
drum_pattern = [
    [36, 38, 42],   # Kick, snare, hihat
    [42],           # Hihat
    [36, 38, 42],   # Kick, snare, hihat
    [38, 42],       # Snare, hihat
    [36, 38, 42],   # Kick, snare, hihat
    [42],           # Hihat
    [36, 38, 42],   # Kick, snare, hihat
    [38, 42],       # Snare, hihat
    [36, 38, 42],   # Kick, snare, hihat
    [42],           # Hihat
    [36, 38, 42],   # Kick, snare, hihat
    [38, 42]        # Snare, hihat
]
for i, notes in enumerate(drum_pattern):
    for pitch in notes:
        note = pretty_midi.Note(velocity=100 if pitch in [36, 38] else 80, pitch=pitch, start=(i * 0.375) + 1.5, end=(i + 1) * 0.375 + 1.5)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
