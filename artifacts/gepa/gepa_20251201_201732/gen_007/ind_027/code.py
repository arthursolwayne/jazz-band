
import pretty_midi

# Initialize a PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set tempo to 160 BPM
pm.bpm = 160

# Define the key (D Major)
tonic = 'D'

# Define note values in MIDI pitch numbers
note_map = {
    'C': 60, 'C#': 61, 'Db': 61,
    'D': 62, 'D#': 63, 'Eb': 63,
    'E': 64, 'F': 65, 'F#': 66, 'Gb': 66,
    'G': 67, 'G#': 68, 'Ab': 68,
    'A': 69, 'A#': 70, 'Bb': 70,
    'B': 71
}

# Define the time per beat and bar
time_per_beat = 0.375  # 160 BPM => 60 / 160 = 0.375 seconds per beat
time_per_bar = 1.5  # 4 beats per bar

# *** INSTRUMENTS ***

# Drums (Little Ray)
drums = pretty_midi.Instrument(program=0)
pm.instruments.append(drums)

# Bass (Marcus)
bass = pretty_midi.Instrument(program=33)
pm.instruments.append(bass)

# Piano (Diane)
piano = pretty_midi.Instrument(program=0)
pm.instruments.append(piano)

# Tenor Sax (You)
sax = pretty_midi.Instrument(program=64)
pm.instruments.append(sax)

# *** BAR 1: Little Ray (Drums) -- Set it up. ***
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
# Bar 1 = 0 to 1.5 seconds
for beat in [0, 2]:
    kick_hit = pretty_midi.Note(
        velocity=100,
        pitch=36,  # Kick
        start=beat * time_per_beat,
        end=beat * time_per_beat + 0.1
    )
    drums.notes.append(kick_hit)

for beat in [1, 3]:
    snare_hit = pretty_midi.Note(
        velocity=100,
        pitch=38,  # Snare
        start=beat * time_per_beat,
        end=beat * time_per_beat + 0.1
    )
    drums.notes.append(snare_hit)

for i in range(0, 4):
    hihat_hit = pretty_midi.Note(
        velocity=90,
        pitch=42,  # Hihat
        start=i * time_per_beat,
        end=i * time_per_beat + 0.05
    )
    drums.notes.append(hihat_hit)

# *** BAR 2: Marcus (Bass) -- Walking line (roots and fifths with chromatic approaches) ***
# Bar 2 = 1.5s to 3.0s
# D, A, D, F# (D Major key)
# Roots and fifths with one chromatic approach each bar

# Bar 2: D -> C# (chromatic approach)
bass_note = pretty_midi.Note(
    velocity=80,
    pitch=note_map['D'],
    start=1.5,
    end=1.5 + 0.25
)
bass.notes.append(bass_note)

bass_note = pretty_midi.Note(
    velocity=80,
    pitch=note_map['C#'],
    start=1.75,
    end=1.75 + 0.25
)
bass.notes.append(bass_note)

# Bar 3: A -> G# (chromatic approach)
bass_note = pretty_midi.Note(
    velocity=80,
    pitch=note_map['A'],
    start=2.0,
    end=2.0 + 0.25
)
bass.notes.append(bass_note)

bass_note = pretty_midi.Note(
    velocity=80,
    pitch=note_map['G#'],
    start=2.25,
    end=2.25 + 0.25
)
bass.notes.append(bass_note)

# Bar 4: D -> C# (chromatic approach)
bass_note = pretty_midi.Note(
    velocity=80,
    pitch=note_map['D'],
    start=2.5,
    end=2.5 + 0.25
)
bass.notes.append(bass_note)

bass_note = pretty_midi.Note(
    velocity=80,
    pitch=note_map['C#'],
    start=2.75,
    end=2.75 + 0.25
)
bass.notes.append(bass_note)

# *** BAR 2: Diane (Piano) -- Open voicings, resolve on the last bar ***
# Comp on beats 2 and 4 (Bar 2, Bar 3, Bar 4)
# Chords: D7, G7, C7 (each bar), resolve on the last chord

# Bar 2: D7 (open voicing)
# D, F#, A, C
d7 = [note_map['D'], note_map['F#'], note_map['A'], note_map['C']]
for pitch in d7:
    note = pretty_midi.Note(
        velocity=90,
        pitch=pitch,
        start=1.5,
        end=1.5 + 0.25
    )
    piano.notes.append(note)

# Bar 3: G7 (open voicing)
# G, B, D, F
g7 = [note_map['G'], note_map['B'], note_map['D'], note_map['F']]
for pitch in g7:
    note = pretty_midi.Note(
        velocity=90,
        pitch=pitch,
        start=2.0,
        end=2.0 + 0.25
    )
    piano.notes.append(note)

# Bar 4: C7 (open voicing)
# C, E, G, Bb
c7 = [note_map['C'], note_map['E'], note_map['G'], note_map['Bb']]
for pitch in c7:
    note = pretty_midi.Note(
        velocity=90,
        pitch=pitch,
        start=2.5,
        end=2.5 + 0.25
    )
    piano.notes.append(note)

# *** BAR 2: You (Tenor Sax) -- One short motif, make it sing ***
# Make it sing: D - F# - A - D (melody), leave it hanging on A, then return to finish

# Bar 2 (start at 1.5s)
note = pretty_midi.Note(
    velocity=100,
    pitch=note_map['D'],
    start=1.5,
    end=1.5 + 0.25
)
sax.notes.append(note)

note = pretty_midi.Note(
    velocity=100,
    pitch=note_map['F#'],
    start=1.75,
    end=1.75 + 0.25
)
sax.notes.append(note)

note = pretty_midi.Note(
    velocity=100,
    pitch=note_map['A'],
    start=2.0,
    end=2.0 + 0.75
)
sax.notes.append(note)

note = pretty_midi.Note(
    velocity=100,
    pitch=note_map['D'],
    start=2.75,
    end=2.75 + 0.25
)
sax.notes.append(note)

# Save the MIDI file
pm.write("Intro_Whisper_Before_Storm.mid")
