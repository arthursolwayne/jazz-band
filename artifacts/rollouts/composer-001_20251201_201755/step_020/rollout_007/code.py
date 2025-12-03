
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
drum_notes = []
for beat in range(4):
    time = beat * 0.375
    if beat % 2 == 0:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125))
    else:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125))
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = []
bass_chords = [
    ('D', 38),   # D2
    ('A', 43),   # A2 (fifth of D)
    ('E', 40),   # E2 (chromatic approach to F)
    ('F', 41),   # F2 (root of G)
    ('G', 43),   # G2 (fifth of C)
    ('C', 40),   # C2 (chromatic approach to B)
    ('B', 42),   # B2 (fifth of F)
    ('F', 41),   # F2 (root of G)
]
for i, (note, pitch) in enumerate(bass_chords):
    time = 1.5 + (i * 0.375)
    bass_notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.125))
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = []
chords = [
    ['D', 'F#', 'A', 'C'],   # D7
    ['G', 'B', 'D', 'F'],    # G7
    ['C', 'E', 'G', 'B'],    # Cmaj7
    ['F', 'A', 'C', 'E'],    # F7
]
for bar, chord in enumerate(chords):
    start = 1.5 + (bar * 1.5)
    for note in chord:
        if note == 'D': pitch = 62
        elif note == 'F#': pitch = 66
        elif note == 'A': pitch = 69
        elif note == 'C': pitch = 60
        elif note == 'G': pitch = 67
        elif note == 'B': pitch = 71
        elif note == 'E': pitch = 64
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 1.5))
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(3):  # Bars 2, 3, 4
    for beat in range(4):
        time = 1.5 + (bar * 1.5) + (beat * 0.375)
        if beat % 2 == 0:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        else:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))
drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = []
# Bar 2: Start motif
sax_notes.append(pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.5 + 0.5))  # D5
# Bar 3: Leave it hanging
sax_notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.0 + 0.25))  # E5
# Bar 4: Come back and finish it
sax_notes.append(pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.5 + 0.5))  # C5
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
